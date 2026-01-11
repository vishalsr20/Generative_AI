# from google import genai
# from google.genai  import types


# client = genai.Client()

# respone = client.models.generate_content(
#     model="gemini-2.5-flash" , contents="Why the sky is blue"
# )

# print(respone.text)

from dotenv import load_dotenv
import os
from google import genai 
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

respone = client.models.generate_content(
    model= "gemini-2.5-flash" , contents="What is the weather in Mumbai ?"
)

print(respone.text)