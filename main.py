import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import call_function, available_functions

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("API KEY wasn't found.")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=messages,
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        temperature=0,
        tools=[available_functions]
    )
)

candidate = response.candidates[0]
tool_results = []

if candidate.content.parts:
    for part in candidate.content.parts:
        if part.function_call:
            function_call_result = call_function(part.function_call, verbose=args.verbose)
            
            if not function_call_result.parts:
                raise Exception("Function call result has no parts")
            
            f_res = function_call_result.parts[0].function_response
            if f_res is None or f_res.response is None:
                raise Exception("Invalid function response structure")
            
            tool_results.append(function_call_result.parts[0])
            
            if args.verbose:
                print(f"-> {f_res.response}")
        elif part.text:
            print(part.text)