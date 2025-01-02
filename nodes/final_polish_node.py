from chains.final_polish_chain import final_polish_chain

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

def final_polish_node(state):
    """take the initial prompt and write a plan to make a long doc"""
    print("---FINAL POLISH---")
    initial_prompt = state['initial_prompt']
    pre_polish_doc = state['pre_polish_doc']
    style = state['style']
    num_steps = int(state['num_steps'])
    num_steps += 1

    final_doc = final_polish_chain.invoke({"instructions": initial_prompt, "content": pre_polish_doc, "style": style})

    # Count words in the final document
    word_count = count_words(final_doc)

    return {"final_doc": final_doc, "word_count": word_count, "num_steps":num_steps}
