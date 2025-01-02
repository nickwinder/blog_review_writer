import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from LLMs.llm import LLM

# Load the reduce_research prompt template
with open(os.path.join(os.path.dirname(__file__), 'prompts', 'reduce_research.txt'), 'r') as file:
    write_template = file.read()

# Create a ChatPromptTemplate
reduce_research = ChatPromptTemplate([
    ('user', write_template)
    ])

# Create the write chain
reduce_research_chain = reduce_research | LLM | StrOutputParser()