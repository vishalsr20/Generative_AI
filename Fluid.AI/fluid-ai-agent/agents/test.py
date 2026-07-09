import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("API Key Loaded:", api_key is not None)

client = genai.Client(api_key=api_key)

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Say Hello"
    )

    print(response.text)

except Exception as e:
    print(type(e).__name__)
    print(e)