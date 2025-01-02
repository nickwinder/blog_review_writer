import os
from dotenv import load_dotenv

# from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_fireworks import ChatFireworks
# from langchain_ollama import ChatOllama

# Load environment variables from .env file
load_dotenv()

# Initialize LLM
# LLM = ChatGroq(model="llama-3.1-70b-versatile",
#                     temperature=0)

gpt4oMini = ChatOpenAI(model="gpt-4o-mini", temperature=0)

gpt4o = ChatOpenAI(model="gpt-4o", temperature=0)
gpt4oWriter = ChatOpenAI(model="gpt-4o", temperature=0.7)

# LLM = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash-exp-0827",
#     temperature=0,
#     )


# FIREWORKS_LLM = ChatFireworks(model="accounts/fireworks/models/llama-v3-70b-instruct")

# OLLAMA_LLM = ChatOllama(model="llama3.1",
#                         temperature=0,
#                         # format="json"
#                         )
