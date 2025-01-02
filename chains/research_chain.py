import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LLMs.llm import LLM

from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.runnables import RunnablePassthrough


# Load the research prompt template
with open(os.path.join(os.path.dirname(__file__), 'prompts', 'research.txt'), 'r') as file:
    research_template = file.read()

# Create the research prompt
research_prompt = ChatPromptTemplate([
    ('user', research_template)
])

# Initialize DuckDuckGo search
search = DuckDuckGoSearchResults()

# Create the topic extraction chain
topic_prompt = ChatPromptTemplate.from_template(
    """Extract 3-5 key topics to research from these writing instructions. Return them as a JSON array of strings.

    Instructions: {instructions}

    Format the response as:
    {{"topics": ["topic1", "topic2", "topic3"]}}"""
)
topic_chain = topic_prompt | LLM | JsonOutputParser()

# Create the research chain that combines everything
def research_chain_fn(inputs):
    return {"instructions": inputs["instructions"]}

research_chain = (
    RunnablePassthrough.assign(
        topics=lambda x: topic_chain.invoke({"instructions": x["instructions"]})
    )
    | RunnablePassthrough.assign(
        search_results=lambda x: [
            {"topic": topic, "results": search.run(topic)} 
            for topic in x["topics"]
        ]
    )
    | research_prompt
    | LLM
    | StrOutputParser()
)
