from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

import os
llm = ChatOpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))


def extract_claims(text):
    prompt = PromptTemplate.from_template("""
    Extract distinct factual medical or statistical claims from this text:
    ---
    {text}
    ---
    List each claim as a bullet point.
    """)
    return llm.predict(prompt.format(text=text))
