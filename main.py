import os
import argparse
from google.genai import types
from prompts import system_prompt
from agent_call import llm_call

parser = argparse.ArgumentParser(description="Coding bot")
parser.add_argument("user_prompt", type=str, help="Tell me whatever you wanna ask..")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
    
def main():
    flag = True
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    for _ in range(20):
        flag = llm_call(system_prompt=system_prompt, args=args, flag=flag, contents=messages)
        if not flag:
            break
    if flag:
        exit(code=1)


if __name__ == "__main__":
    main()
