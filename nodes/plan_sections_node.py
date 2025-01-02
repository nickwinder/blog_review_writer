from chains.plan_sections_chain import plan_sections_chain

def format_responses(responses):
    """Formats a list of responses into a numbered paragraph string."""
    formatted_plan = ""
    index = 1
    for response_text in responses:
        formatted_plan += f"Paragraph {index} - {response_text}\n\n"
        index += 1
    return formatted_plan

def plan_sections_node(state):
    """take the initial prompt and write a plan to make a long doc"""
    print("---PLANNING THE WRITING---")
    research = state['research']
    overview = state['overview']
    num_steps = int(state['num_steps'])
    num_steps += 1

    overview = overview.strip().replace('\n\n', '\n')
    overview_steps = overview.split('\n')
    plan = ""
    responses = []

    for idx, overview_step in enumerate(overview_steps):
        print(f"----------------------------{idx}----------------------------")
        print(overview_step)
        print("----------------------------\n\n")

        result = plan_sections_chain.invoke({"overview": overview, "plan": plan, "research": research, "STEP": overview_step})
        result = result.strip().replace('\n\n', '\n')
        result_steps = result.split('\n')
        responses.extend(result_steps)
        plan = format_responses(responses)
        print(result + '\n')

    return {"plan": plan, "num_steps":num_steps}
