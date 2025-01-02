from langgraph.graph import StateGraph, END
from typing_extensions import TypedDict
from typing import List

from nodes.overview_plan_node import overview_plan_node
from nodes.writing_node import writing_node
from nodes.saving_node import saving_node
from nodes.plan_sections_node import plan_sections_node
from nodes.final_polish_node import final_polish_node


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        initial_prompt: initial prompt
        plan: plan
        num_steps: number of steps
        post_name: name of the LLM
        word_count: word count of the final document
    """
    initial_prompt : str
    overview : str
    plan : str
    num_steps : int
    pre_polish_doc : str
    final_doc : str
    write_steps : List[str]
    word_count : int
    post_name : str
    research : str
    style: str



def create_workflow():
    workflow = StateGraph(GraphState)

    # Add nodes
    # workflow.add_node("research_node", research_node)
    workflow.add_node("overview_planning_node", overview_plan_node)
    workflow.add_node("plan_sections_node", plan_sections_node)
    workflow.add_node("writing_node", writing_node)
    workflow.add_node("final_polish_node", final_polish_node)
    workflow.add_node("saving_node", saving_node)

    # Set entry point
    # workflow.set_entry_point("research_node")
    workflow.set_entry_point("overview_planning_node")

    # Add edges
    # workflow.add_edge("research_node", "planning_node")
    workflow.add_edge("overview_planning_node", "plan_sections_node")
    workflow.add_edge("plan_sections_node", "writing_node")
    workflow.add_edge("writing_node", "final_polish_node")
    workflow.add_edge("final_polish_node", "saving_node")
    workflow.add_edge("saving_node", END)

    return workflow.compile()