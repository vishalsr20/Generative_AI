from services.gemini_services import generate_response


def review_document(document: str):

    prompt = f"""
You are a senior technical reviewer.

Review the following business document.

Check:

1. Is the document complete?

2. Does it have all important sections?

3. Is the grammar professional?

4. Is the formatting logical?

5. Is the tone suitable for business?

Return ONLY JSON.

Format:

{{
    "status":"PASS",

    "feedback":"..."
}}

If the document has major issues

return

{{
    "status":"FAIL",

    "feedback":"..."
}}

Document:

{document}
"""

    response = generate_response(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")

    import json

    return json.loads(response)