
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

system_prompt = """
You are an expert problem-solving assistant.

You must reason internally but do NOT reveal internal chain-of-thought.

Return a structured explanation in STRICT JSON.

Steps (in order):
analysis
approach
solution
validation
result

Rules:
- Output ONLY valid JSON
- Follow step order strictly
- Do not add extra text

JSON format:
{
  "step": "string",
  "content": "string"
}
"""

user_question = "What is 3 + 4 * 5?"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        {
            "role": "user",
            "parts": [{
                "text": system_prompt + "\n\nUser question:\n" + user_question
            }]
        }
    ]
)

print(response.text)
