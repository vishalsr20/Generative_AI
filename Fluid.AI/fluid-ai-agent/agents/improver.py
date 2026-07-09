from services.gemini_services import generate_response


def improve_document(document: str, feedback: str):

    prompt = f"""
You are a senior technical writer.

Improve the following document using this feedback.

Feedback:

{feedback}

Document:

{document}

Return ONLY the improved document.
"""

    return generate_response(prompt)