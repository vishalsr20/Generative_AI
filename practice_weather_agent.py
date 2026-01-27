from dotenv import load_dotenv
from groq import Groq
import os
import json
import requests
load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

def get_weather(city:str):
    url = "https://wttr.in/{city}?format=%C+t%22"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in  {city} is {response.text}."
    return "31 Degree Celcius"

def run_command(ls):
    return 0


available_tools = {
    "get_weather":{
        "fn":get_weather,
        "description":"Take a city name as an input and return the current weather iif the city"
    },
    "run_command":{
        "fn":run_command,
        "decription":"Take a command as input to execute on the system and return output"
    }
}


system_prompt = """
    You are a helpful AI Assistant who is specialized in resolving user query.
    You work on start , plan , action , observe mode.
    For the given user query and available tools , plan the step by step execution based on the planning,
    select the relevent tool from the available tool , and based on the tool selection you perfrom an acction to call the tool.
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
        "input":"The input parameter for the function"
    }}

    Available Tools:
    - get_weather : Take a city as an input and return the weather for the city.


    Example : 
    User Query : What is the weather of the new york?
    Output:{{"step":"plan","content:"The user is interested in weather data of the new york"}}
    Output:{{"step":"plan", "content":"From the available tools, I should call the get_weather"}}
    Output:{{"step":"action", "function":"get_weather", "input":"new york"}}
    Output:{{"step":"observe","output":"12 Degree Celcius"}}
    Output:{{"step":"output","content":"The weather of the new york is 12 Degree celcius}}

"""

messages = [
    {"role":"system", "content":system_prompt}
]

user_query = input('> ')
messages.append({"role":"user","content":user_query})

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    response_format = {"type":"json_object"},
    # messages=[
    #     {"role":"system", "content":system_prompt},
    #     {"role":"user", "content":"Hello , I am Vishal , what is the weather of navi-mumbai?"},
    #     {"role":"assistant","content":json.dumps({"step":"plan","content":"The user wants the weather for Navi Mumbai"})}
    # ]
    messages=messages
)

print(response.choices[0].message.content)
