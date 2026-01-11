import os
import sys
import argparse
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("API KEY wasn't found.")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="AI Agent")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

# Start konverzace
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

for i in range(20):
    if i > 0:
        time.sleep(1) # Ochrana proti kvótě

    response = client.models.generate_content(
        model='gemini-2.5-flash', # Použij svůj fungující model
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0,
            tools=[available_functions]
        )
    )

    if not response.candidates or not response.candidates[0].content:
        break

    # 1. Uložíme odpověď modelu (plánování funkce) do historie
    messages.append(response.candidates[0].content)
    
    candidate = response.candidates[0]
    function_responses = []

    # 2. Provádění volání funkcí
    if candidate.content.parts:
        for part in candidate.content.parts:
            if part.function_call:
                # Spustíme funkci a získáme Content s rolí 'tool'
                call_result_content = call_function(part.function_call, verbose=args.verbose)
                # Důležité: Vezmeme jen Part (function_response)
                function_responses.append(call_result_content.parts[0])

    # 3. Rozhodnutí o dalším kroku
    if function_responses:
        # PŘIDÁME VÝSLEDEK JAKO ROLI 'user' (nutné pro kontext v Gemini SDK)
        messages.append(types.Content(role="user", parts=function_responses))
        # Loop pokračuje -> model teď vidí výsledek get_files_info a řekne si o get_file_content
        continue
    else:
        # Model už nic volat nechce, vypíšeme finální text
        final_text = ""
        if candidate.content.parts:
            final_text = "".join([p.text for p in candidate.content.parts if p.text])
        
        # Pokud model vrátí prázdný text po volání funkcí (časté), vypíšeme response.text
        if not final_text:
            final_text = response.text or "Agent has completed the task."

        print(f"\nFinal response:\n{final_text}")
        break
else:
    print("Error: Maximum iterations reached.")
    sys.exit(1)