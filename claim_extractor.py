import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

def extract_claims(text: str) -> str:
    prompt = PromptTemplate.from_template("""
    Extract distinct factual medical or statistical claims from this text:
    ---
    {text}
    ---
    List each claim as a bullet point.
    """)
    # The OpenAI LLM uses __call__, so invoke it directly:
    return llm(prompt.format(text=text))
