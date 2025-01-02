import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LLMs.llm import gpt4oMini

from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Load the plan prompt template
with open(os.path.join(os.path.dirname(__file__), 'prompts', 'plan_sections.txt'), 'r') as file:
    plan_template = file.read()

# Create a PromptTemplate
plan_sections_prompt = ChatPromptTemplate([
        ('user', plan_template)
    ])


plan_sections_chain = plan_sections_prompt | gpt4oMini | StrOutputParser()


## For testing
if __name__ == "__main__":
    # Test the plan_chain
    test_instruction = "Write a current and up to date 100% unique guide for my intermittent fasting for women over 50 cookbook on \u201cSnacks\u201d with humanlike style, using transitional phrases, and avoidance of unnatural sentence structure while explaining in details extensively and comprehensively."
    
    # Invoke the plan_chain
    result = plan_sections_chain.invoke({"instructions": test_instruction, "research": "No one should fast"})
    
    # Print the result
    print("Generated Writing Plan:")
    print(result)


