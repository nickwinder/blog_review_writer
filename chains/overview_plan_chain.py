import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LLMs.llm import gpt4oMini

from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Load the plan prompt template
with open(os.path.join(os.path.dirname(__file__), 'prompts', 'overview_plan.txt'), 'r') as file:
    plan_template = file.read()

# Create a PromptTemplate
overview_plan_prompt = ChatPromptTemplate([
        ('user', plan_template)
    ])


overview_plan_chain = overview_plan_prompt | gpt4oMini | StrOutputParser()


## For testing
if __name__ == "__main__":
    # Test the plan_chain
    test_instruction = (
        "Write a 1500 word comprehensive review of the Altra King MT 2 with humanlike style, using transitional phrases, and avoidance of unnatural sentence structure while explaining in details extensively and comprehensively.\n"
        "The review should have 5 major sections: Introduction, Fit, Feel, Durability, and Conclusion. The latter 4 should be heading 2 (`##`) There should be no other headings in the text. \n"
        "Introduction - Should be short containing 5-6 sentences on single lines teasing some of the key features of the model, and enticing the reader to keep reading.\n"
        "Fit - A section of around 500 words with multiple paragraphs each focusing on different aspects of the shoe fit. Ensure you cover the suggested sizing (for example true to size, or 1/2 size up or down), the width in different areas of the shoe, and depth in different areas of the shoe. Each paragraph should be 2-3 sentences, and the first sentence should be bolded to allow the section to be skimmable by the reader.\n"
        "Feel - A section of around 500 words with multiple paragraphs each focusing on a different aspect of the feel of the shoe. This could be flexibility, stiffness, grip, stackheight etc. Each paragraph should be 2-3 sentences, and the first sentence should be bolded to allow the section to be skimmable by the reader.\n"
        "Durability - A section of around 500 words with multiple paragraphs each focusing on a different aspect of the durability of the shoe. Focus on the outsole, midsole if it has one, and the upper construction of the shoe. Each paragraph should be 2-3 sentences, and the first sentence should be bolded to allow the section to be skimmable by the reader.\n"
        "Conclusion - Wrap up the review suggesting some final thoughts and what other shoes a user should consider.")

    # Invoke the plan_chain
    result = overview_plan_chain.invoke({"instructions": test_instruction})
    
    # Print the result
    print("Generated Writing Plan:")
    print(result)


