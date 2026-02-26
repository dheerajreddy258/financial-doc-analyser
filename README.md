# Financial Document Analyzer - AI-Powered Analysis System

A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using CrewAI with AI-powered analysis agents powered by Groq API (Mixtral).

## 🎯 Quick Start

### Requirements
- Python 3.10+
- Groq API Key

### Setup (3 steps)

```bash
# 1. Clone and setup
git clone <repo-url>
cd financial-doc-analyser
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure API key
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
```

### Run
```bash
python main.py
# API available at http://localhost:8000
```

---

## 📋 What's Fixed

This project had **9 bugs** that have all been resolved:

### Deterministic Bugs Fixed:
1. ✅ **Circular LLM initialization** - Now uses ChatGroq properly
2. ✅ **Wrong parameter name** - Fixed `tool=` to `tools=` across agents
3. ✅ **Undefined PDF class** - Implemented proper PyPDF integration
4. ✅ **Async function issues** - Corrected function signatures
5. ✅ **Function name collision** - Separated endpoint from imported task
6. ✅ **Missing dependencies** - Added uvicorn, python-dotenv, pypdf, langchain-groq, groq
7. ✅ **Inefficient string handling** - Optimized from O(n²) to O(n)

### Inefficient Prompts Fixed:
8. ✅ **Sarcastic agent roles** - Rewrote with professional, accurate descriptions
9. ✅ **Vague task descriptions** - Created detailed, structured task prompts

**[See detailed bug analysis in README_BUGS_FIXED.md]**

---

## 🚀 API Usage

### Health Check
```bash
curl http://localhost:8000/
```

### Analyze Document
```bash
curl -X POST "http://localhost:8000/analyze" \
  -F "file=@data/sample.pdf" \
  -F "query=Provide investment recommendations"
```

Interactive docs: http://localhost:8000/docs

---

## 📊 Features

- **Financial Analysis** - Comprehensive document analysis
- **Investment Insights** - Evidence-based recommendations
- **Risk Assessment** - Multi-dimensional risk evaluation
- **Document Verification** - Validate financial documents
- **Market Context** - Web search integration

---

## 🏗️ Architecture

**Multi-Agent System:**
- Financial Analyst (Core analysis)
- Document Verifier (Quality control)
- Investment Advisor (Recommendations)
- Risk Assessor (Risk evaluation)

---

## 📁 Project Structure

```
financial-doc-analyser/
├── main.py              # FastAPI server
├── agents.py            # Agent definitions
├── tasks.py             # Task definitions
├── tools.py             # Custom tools
├── requirements.txt     # Dependencies
├── .env                 # Environment variables
├── data/                # Document storage
│── README.md            # This file
└── README_BUGS_FIXED.md # Detailed analysis
```

---

## 🔧 Configuration

### Environment Variables
```bash
GROQ_API_KEY=your_groq_api_key  # Required (get from https://console.groq.com)
```

> **⚠️ Make sure the key is valid and current.**
> Groq keys begin with `gsk_…` and must be copied exactly from the
> Groq dashboard. Using an OpenAI key or a malformed/expired Groq key
> will result in authentication errors (see troubleshooting section below).

### Troubleshooting
- `AuthenticationError: Incorrect API key provided` – usually means the
  value in `GROQ_API_KEY` is wrong. Re‑export the correct key and restart
  the server.
- `400 Bad Request` from Groq normally indicates a missing `groq/`
  prefix on the model name or an invalid model string.

### Adjust LLM Settings (agents.py)
```python
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.5,  # 0=deterministic, 1=creative
    groq_api_key=os.getenv("GROQ_API_KEY")
)
```

---

## 📚 Supported Documents

- 📊 Earnings Reports (10-Q, 10-K)
- 📈 Financial Statements
- 💼 Proxy Statements (14-A)
- 📑 Market Analysis Reports
- 💰 Investment Prospectuses
- 📄 Annual Reports

---

## 🧪 Testing

### Manual Test
1. Start server: `python main.py`
2. Open http://localhost:8000/docs
3. Upload a PDF via the interface
4. Enter analysis query
5. Review results

### Example Query
```
"Analyze the financial health and provide investment recommendation"
```

Expected: Comprehensive financial analysis with investment insights

---

---

## 📦 Dependencies

Key packages:
- `crewai` (0.130.0) - Multi-agent framework
- `fastapi` (0.110.3) - Web framework
- `langchain-groq` (0.1.9) - Groq integration
- `groq` (0.5.0) - Groq Python client
- `pypdf` (4.1.1) - PDF processing
- `python-dotenv` - Environment configuration
- `uvicorn` - ASGI server

For complete list, see `requirements.txt`

---



---

## 🤝 Contributing

Bug reports and feature requests are welcome! Please open an issue on GitHub.

---


---

## 📊 Bug Fixes Summary

| Bug # | Type | File | Issue | Status |
|-------|------|------|-------|--------|
| 1 | Deterministic | agents.py | Circular LLM assignment | ✅ Fixed |
| 2 | Deterministic | agents.py | Wrong parameter name | ✅ Fixed |
| 3 | Deterministic | tools.py | Undefined Pdf class | ✅ Fixed |
| 4 | Deterministic | tools.py | Async function issues | ✅ Fixed |
| 5 | Deterministic | main.py | Function name collision | ✅ Fixed |
| 6 | Deterministic | requirements.txt | Missing dependencies | ✅ Fixed |
| 7 | Inefficient | tools.py | O(n²) space manipulation | ✅ Fixed |
| 8 | Inefficient Prompt | agents.py | Sarcastic agent roles | ✅ Fixed |
| 9 | Inefficient Prompt | task.py | Vague task descriptions | ✅ Fixed |

**Total: 9 bugs resolved** ✅

---

**Status:** ✅ All bugs fixed and ready for deployment

For detailed technical analysis of bugs fixed, see [README_BUGS_FIXED.md](README_BUGS_FIXED.md)
