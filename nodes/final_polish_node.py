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
    subject = state['subject']
    pre_polish_doc = state['pre_polish_doc']
    style = state['style']
    structure = state['structure']
    num_steps = int(state['num_steps'])
    num_steps += 1

    final_doc = final_polish_chain.invoke({"subject": subject, "content": pre_polish_doc, "style": style, "structure": structure})

    # Count words in the final document
    word_count = count_words(final_doc)

    return {"final_doc": final_doc, "word_count": word_count, "num_steps":num_steps}
