from dotenv import load_dotenv
from langchain_core.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from langchain import hub
from langchain_core.prompts import PromptTemplate
from tools import get_profile_url
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)

load_dotenv()

def lookup(name: str) -> str:
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        convert_system_message_to_human=True,
        temperature=0,
        streaming=True,
    )

    template = """Given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page. Your answer should contain only a URL."""

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google for LinkedIn profile page",
            func=get_profile_url,
            description="Useful for when you need get the Linkedin Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linked_profile_url = result["output"]
    print(linked_profile_url)
    return linked_profile_url

lookup("Elon Musk")

