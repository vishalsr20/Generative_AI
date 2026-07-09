from services.gemini_services import generate_response


def execute_plan(user_request: str, plan: dict) -> str:
    tasks = "\n".join([f"- {task}" for task in plan["tasks"]])
    assumptions = "\n".join([f"- {a}" for a in plan["assumptions"]])

    prompt = f"""
You are an autonomous AI execution agent.

The user requested:

{user_request}

Execution Plan:
{tasks}

Assumptions:
{assumptions}

Follow the execution plan and generate a professional business document.

Requirements:
- Use clear headings.
- Use professional language.
- Organize the content logically.
- Include a conclusion.
- Return ONLY the document content.
"""

    return generate_response(prompt)