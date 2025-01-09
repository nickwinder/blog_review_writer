from langchain_core.documents import Document
from chains.research_chain import research_chain


def research_node(state):
    """take the initial prompt and perform searches to research the topic"""
    print("---RESEARCHING THE WRITING---")
    subject = state['subject']
    num_steps = int(state['num_steps'])
    num_steps += 1

    research = research_chain.invoke({"subject": subject})
    print(research)

    return {"research": research, "num_steps":num_steps}
