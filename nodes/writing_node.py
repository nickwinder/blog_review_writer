from langchain_core.documents import Document
from chains.write_chain import write_chain

def count_words(text):
        """
        Count the number of words in the given text.
        
        Args:
            text (str): The input text to count words from.
        
        Returns:
            int: The number of words in the text.
        """
        # Split the text into words and count them
        words = text.split()
        return len(words)

def writing_node(state):
    """take the initial prompt and write a plan to make a long doc"""
    print("---WRITING THE DOC---")
    initial_instruction = state['initial_prompt']
    research = state['research']
    overview = state['overview']
    plan = state['plan']
    num_steps = int(state['num_steps'])
    num_steps += 1

    plan = plan.strip().replace('\n\n', '\n')
    planning_steps = plan.split('\n')
    text = ""
    responses = []
    if len(planning_steps) > 50:
        print("plan is too long")
        # print(plan)
        return
    for idx,step in enumerate(planning_steps):
        # Invoke the write_chain
        result = write_chain.invoke({
            "instructions": initial_instruction,
            "overview": overview,
            "research": research,
            "plan": plan,
            "text": text,
            "STEP": step
        })
        # result = step
        print(f"----------------------------{idx}----------------------------")
        print(step)
        print("----------------------------\n\n")
        responses.append(result)
        text += result + '\n\n'

    pre_polish_doc = '\n\n'.join(responses)

    # Count words in the final document
    word_count = count_words(pre_polish_doc)

    return {"pre_polish_doc": pre_polish_doc, "word_count": word_count, "num_steps":num_steps}



