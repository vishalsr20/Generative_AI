import json

from services.gemini_services import generate_response


def create_plan(user_request: str):

    prompt = f"""
You are an autonomous AI planning agent.

Your job is NOT to solve the request.

Instead,

1. Understand the request.

2. Break it into executable tasks.

3. Identify reasonable assumptions.

Return ONLY valid JSON.

Example:

{{
    "tasks": [
        "task1",
        "task2"
    ],
    "assumptions": [
        "assumption1"
    ]
}}

User Request:

{user_request}
"""


    response = generate_response(prompt)
    response = response.replace("```json", "").replace("```", "").strip()
    return json.loads(response)