import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    temperature=0.7,
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile"
)