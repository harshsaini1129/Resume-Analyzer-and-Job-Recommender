# AI Job Recommender🚀

An AI-powered Resume Analyzer & Job Recommendation System that analyzes your resume and recommends relevant jobs from LinkedIn & Naukri using Generative AI.

Built using Streamlit + OpenRouter + Apify + PyMuPDF + MCP Server.

 Features

✅ Upload Resume (PDF)
✅ Automatic Resume Text Extraction
✅ AI Resume Summary
✅ Skill Gap Analysis
✅ Future Career Roadmap
✅ Job Recommendations from LinkedIn & Naukri
✅ MCP Server Integration for AI Tool Access
✅ Simple Streamlit UI

# Tech Stack🛠️
Layer	Technology
Frontend	Streamlit
Backend	Python
AI Model	OpenRouter (GPT-OSS-120B)
Resume Parsing	PyMuPDF (fitz)
Job Scraping	Apify (LinkedIn + Naukri actors)
Env Management	dotenv
MCP Server	FastMCP
Deployment Ready	Docker / AWS EC2

# Project Structure
AIJOB_RECOMMENDER/
│
├── src/
│   ├── __init__.py
│   ├── helper.py        # PDF extraction + OpenRouter API calls
│   ├── job_api.py       # LinkedIn & Naukri scraping functions
│
├── app.py               # Streamlit main app
├── mcpserver.py         # MCP server exposing job tools
│
├── .env                 # API keys
├── requirements.txt     # Dependencies
├── pyproject.toml
├── uv.lock
├── .gitignore
├── .python-version
└── README.md

# How It Works

1️⃣ User uploads resume (PDF)
2️⃣ PyMuPDF extracts resume text
3️⃣ OpenRouter AI analyzes resume
4️⃣ AI generates job keywords
5️⃣ Apify scrapes jobs from LinkedIn & Naukri
6️⃣ Streamlit displays results

# Required API Keys

Create .env file in root folder:

OPENROUTER_API_KEY=your_openrouter_api_key
APIFY_API_KEY=your_apify_api_key


Get Keys From:

https://openrouter.ai/

https://apify.com/

💻 Installation Guide
1️⃣ Clone Repository
git clone https://github.com/harshsaini1129/aijob-recommender.git
cd aijob-recommender

2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Application

streamlit run app.py

