import os
import argparse
from typing import Any
from google import genai
from prompts import system_prompt
from call_function import available_functions
from google.genai import types
from dotenv import load_dotenv

parser = argparse.ArgumentParser(description="Coding bot")
parser.add_argument("user_prompt", type=str, help="Tell me whatever you wanna ask..")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

load_dotenv()
try:
    api_key = os.environ.get("GEMINI_API_KEY")
except:
    raise RuntimeError()

client = genai.Client(api_key=api_key)

def llm_call(system_prompt: str, args, contents: list[Any], model_name: str = "gemini-2.5-flash") -> str:
    """
    Docstring for llm_call
    
    :param prompt: Prompt to the llm
    :type prompt: str
    :return: response from the llm
    :rtype: str
    """
    response =  client.models.generate_content(
                model=model_name,
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    tools=[available_functions]
                    ),
                )
    
    if response.usage_metadata:
        token_sent = response.usage_metadata.prompt_token_count
        token_received = response.usage_metadata.candidates_token_count
    else:
        raise RuntimeError("Api Call wasn't successfull.")
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {token_sent}")
        print(f"Response tokens: {token_received}")
        print(f"Response:\n{response.text}")
    else:
        if response.function_calls:
            for function_call in response.function_calls:
                print(f"Calling function: {function_call.name}({function_call.args})")
        else:
            print(f"{response.text}")
    
    return response.text
    
    
    
def main():
    # prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    response = llm_call(system_prompt=system_prompt, args=args, contents=messages)


if __name__ == "__main__":
    main()
