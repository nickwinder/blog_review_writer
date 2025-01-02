from chains.overview_plan_chain import overview_plan_chain


def overview_plan_node(state):
    """take the initial prompt and write a plan to make a long doc"""
    print("---OVERVIEW THE WRITING---")
    initial_prompt = state['initial_prompt']
    num_steps = int(state['num_steps'])
    num_steps += 1

    overview = overview_plan_chain.invoke({"instructions": initial_prompt})
    print(overview)

    return {"overview": overview, "num_steps":num_steps}
