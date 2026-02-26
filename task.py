from crewai import Task
from agents import financial_analyst
from tools import FinancialDocumentTool

# Single deterministic task
analyze_financial_document = Task(
    description="""
    Analyze the financial document located at: {file_path}.
    Address the user query: {query}.

    Your analysis must include:

    1. Document Overview:
       - Type of document
       - Reporting period
       - Key entities involved

    2. Financial Performance:
       - Revenue trends
       - Profitability
       - Cash flow observations
       - Growth patterns

    3. Financial Health:
       - Liquidity position
       - Debt levels
       - Operational efficiency

    4. Key Findings:
       - Significant changes
       - Notable trends
       - Financial anomalies (if any)

    5. Risk Factors:
       - Operational risks
       - Financial risks
       - Market risks mentioned in the document

    Important Rules:
    - Use only information from the uploaded document.
    - Do NOT fabricate data.
    - Do NOT invent external sources.
    - Base conclusions strictly on document evidence.
    """,

    expected_output="""
    Provide a structured financial analysis report containing:

    - Executive Summary
    - Key Financial Metrics
    - Performance Analysis
    - Financial Health Assessment
    - Risk Evaluation
    - Conclusion
    """,

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)