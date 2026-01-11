from dotenv import load_dotenv 
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    message=[
        { "role" : "user", "content":"What is the current weather of Mumbai ?"}
    ]
)

print(response.choices[0].message.content)