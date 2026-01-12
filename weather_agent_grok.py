from dotenv import load_dotenv 
from groq import Groq 
import os 
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_weather(city:str):
    return "31 degree celcius"

system_prompt = """
    You are an helpful AI Assistant who is specialized in resolving user query.
    You work on start , plan , action , observe mode.
    For the given user query and available tools, plan the step by step execution based on the planning,
    select the relevant tool from the available  tool. and based on the tool selection you perform an action to call the tool.
    Wait for the observation and based on the observation from the tool call resolve the user query.

    Rules:
    - Follow the Output JSON Format.
    - Always perform one step at a time and wait for the next input.
    - Carefully analyse the user query.

    Output JSON Format:
    {{
        "step":"string",
        "content":"string",
        "function":"The name of function if the step is action",
        "input":"The inout parameter for the function",

    }}

    Available Tools:

    Example:
    User Query : What is the weather of the new york ? 
    Output : {{ "step": "plan" , "content":"The user is inetrested in  weather data of the new york"}}
    Output : {{"step": "plan"}, "content":"From the available tools I should call get_weather"}}
    Output: {{"step":"action", "function":"get_weather", "input":"new york"}}
    Output: {{"step":"observe", "output":"12 Degree Cel"}}
    Output : {{ "step": "output", "content":"The weather for the new york seems to be 12 degree." }}
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role":"system", "content":system_prompt},
        { "role" : "user", "content":"What is the current weather of Pune ?"},
        {"role":"assistant", "content": json.dumps({"step": "plan", "content": "The user wants the current weather information for Pune."})},
        {"role":"assistant", "content": json.dumps({"step": "plan", "content": "The previous weather data was for Mumbai, but the user asked for Pune. I need to call get_weather for Pune."})},
        {"role":"assistant", "content": json.dumps({"step": "action", "function": "get_weather", "input": "Pune"})},
        {"role":"assistant", "content": json.dumps({"step": "observe", "output": "30°C, clear sky"})},
    ]
)

print(response.choices[0].message.content)