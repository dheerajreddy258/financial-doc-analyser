import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM
from tools import FinancialDocumentTool

# Initialize CrewAI LLM using Groq provider
# llm = LLM(
#     model="groq/mixtral-8x7b-32768",
#     api_key=os.getenv("GROQ_API_KEY")
# )
llm = LLM(
    # Groq's OpenAI-compatible API requires the model name to include the
    # "groq/" prefix. Using just the bare name results in a 400 Bad Request.
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
)

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze the uploaded financial document and provide structured, evidence-based insights addressing the user query: {query}.",
    verbose=True,
    memory=False,
    backstory=(
        "You are a professional financial analyst specializing in corporate financial reports. "
        "You extract key financial metrics, evaluate performance, assess financial health, "
        "and provide balanced investment insights strictly based on document content."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=3,
    allow_delegation=False
)