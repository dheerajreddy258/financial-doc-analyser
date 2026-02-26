import os
from dotenv import load_dotenv
load_dotenv()

from crewai.tools import tool
from pypdf import PdfReader


class FinancialDocumentTool:

    @staticmethod
    @tool("Read financial document")
    def read_data_tool(path: str) -> str:
        """
        Reads a financial PDF document and returns cleaned text content.

        Args:
            path (str): Path to the uploaded PDF file

        Returns:
            str: Extracted and cleaned document text
        """
        try:
            if not os.path.exists(path):
                return f"Error: File not found at {path}"

            reader = PdfReader(path)

            full_report = ""

            for page_number, page in enumerate(reader.pages):
                content = page.extract_text()

                if content:
                    # Clean extra newlines
                    while "\n\n" in content:
                        content = content.replace("\n\n", "\n")

                    full_report += f"\n--- Page {page_number + 1} ---\n"
                    full_report += content.strip() + "\n"

            if not full_report.strip():
                return "Warning: No readable text found in the PDF."

            return full_report

        except Exception as e:
            return f"Error reading PDF: {str(e)}"