# 🧠 MedFact Agent

Fact-check medical claims with real PubMed citations.

## Setup

1. Clone this repo
2. Create a `.env` file with your OpenAI API key
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the app:
```bash
streamlit run app.py
```

## What It Does

- Extracts medical/statistical claims
- Searches PubMed for evidence
- Returns real citations or flags unverifiable content