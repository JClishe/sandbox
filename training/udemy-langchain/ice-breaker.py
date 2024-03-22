from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from linkedin_lookup_agent import lookup as linkedin_lookup_agent
from linkedin import scrape_linkedin_profile 
import os
import requests

load_dotenv()

linkedin_profile_url = linkedin_lookup_agent(name="Elon Musk")

summary_template = """
Given the information {information} about a person, I want you to create:
1. A short summary
2. Two interesting facts about them
"""

summary_prompt_template = PromptTemplate(
    input_variables=["information"],
    template=summary_template
)

print(linkedin_profile_url)

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    convert_system_message_to_human=True,
    temperature=0.8,
    streaming=True,
    safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    },
)

chain = LLMChain(llm=llm, prompt=summary_prompt_template)

linkedin_data = scrape_linkedin_profile(
    linkedin_profile_url=linkedin_profile_url
    )

print(chain.run(information=linkedin_data))