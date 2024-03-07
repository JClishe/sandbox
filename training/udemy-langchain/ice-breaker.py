from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_google_vertexai import ChatVertexAI, HarmBlockThreshold, HarmCategory
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

# print(os.environ['RANDOM_API_KEY'])

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
# os.environ["GOOGLE_CLOUD_PROJECT"] = "jclishe-sandbox"
# os.environ["GOOGLE_CLOUD_REGION"] = "us-central1"

information = """
Elon Musk (born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect, and former chairman of Tesla, Inc.; owner, executive chairman, and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is one of the wealthiest people in the world, with an estimated net worth of US$213 billion as of February 2024, according to the Bloomberg Billionaires Index, and $210 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX.[5][6]

A member of the wealthy South African Musk family, Elon was born in Pretoria and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University at Kingston in Canada. Musk later transferred to the University of Pennsylvania, and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University, but dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999, and that same year Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal.

In October 2002, eBay acquired PayPal for $1.5 billion, and that same year, with $100 million of the money he made, Musk founded SpaceX, a spaceflight services company. In 2004, he became an early investor in electric vehicle manufacturer Tesla Motors, Inc. (now Tesla, Inc.). He became its chairman and product architect, assuming the position of CEO in 2008. In 2006, Musk helped create SolarCity, a solar-energy company that was acquired by Tesla in 2016 and became Tesla Energy. In 2013, he proposed a hyperloop high-speed vactrain transportation system. In 2015, he co-founded OpenAI, a nonprofit artificial intelligence research company. The following year, Musk co-founded Neuralink—a neurotechnology company developing brain–computer interfaces—and the Boring Company, a tunnel construction company. In 2022, he acquired Twitter for $44 billion. He subsequently merged the company into newly created X Corp. and rebranded the service as X the following year. In March 2023, he founded xAI, an artificial intelligence company.

Musk has expressed views that have made him a polarizing figure.[7] He has been criticized for making unscientific and misleading statements, including COVID-19 misinformation and antisemitic conspiracy theories.[7][8][9][10] His ownership of Twitter has been similarly controversial, being marked by the laying off of a large number of employees, an increase in hate speech and misinformation and disinformation on the website, as well as changes to Twitter Blue verification. In 2018, the U.S. Securities and Exchange Commission (SEC) sued him, alleging that he had falsely announced that he had secured funding for a private takeover of Tesla. To settle the case, Musk stepped down as the chairman of Tesla and paid a $20 million fine.
"""

summary_template = """
Given the information {information} about a person, I want you to create:
1. A short summary
2. Two interesting facts about them
"""

summary_prompt_template = PromptTemplate(input_variables=["information"], template= summary_template)

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    convert_system_message_to_human=True,
    temperature=0.8,
    streaming=True,
    safety_settings={
        HarmCategory.HARM_CATEGORY_UNSPECIFIED: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        },
)

chain = LLMChain(llm=llm, prompt=summary_template)
res = chain.invoke(input={"information": information})

print(res)
