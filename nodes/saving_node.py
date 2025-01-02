import os
from typing import Any, Dict

from langchain_core.documents import Document
from tools.tools import write_markdown_file


def saving_node(state):
    """take the finished long doc and save it to local disk as a .md file   """
    print("---SAVING THE DOC---")
    overview = state['overview']
    plan = state['plan']
    pre_polish_doc = state['pre_polish_doc']
    final_doc = state['final_doc']
    word_count = state['word_count']
    post_name = state['post_name']
    num_steps = int(state['num_steps'])
    num_steps += 1

    final_doc = final_doc + f"\n\nTotal word count: {word_count}"

    output_dir = f"output/{post_name}"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # save to local disk
    write_markdown_file(pre_polish_doc, f"pre_polish_{post_name}", output_dir)
    write_markdown_file(final_doc, f"final_doc_{post_name}", output_dir)
    write_markdown_file(overview, f"overview_{post_name}", output_dir)
    write_markdown_file(plan, f"plan_{post_name}", output_dir)

    return { "num_steps":num_steps}