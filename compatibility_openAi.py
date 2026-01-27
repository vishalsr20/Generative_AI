from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.responses.create(
    model="gemini-1.5-flash",
    input=[
        {
            "role":"system",
            "content":"You are a helpful assistant."
        },
        {
            "role":"user",
            "content":"Explain to me how AI works"
        }
    ]
)

print(response.output_text)