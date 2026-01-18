import os
from typing import Any
from google import genai
from call_function import available_functions, call_function
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
try:
    api_key = os.environ.get("GEMINI_API_KEY")
except:
    raise RuntimeError()

client = genai.Client(api_key=api_key)


def llm_call(system_prompt: str, args, flag: bool, contents: list[Any], model_name: str = "gemini-2.5-flash") -> str:
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
    
    for candidate in response.candidates:
        contents.append(candidate.content)
        
    
    if response.usage_metadata:
        token_sent = response.usage_metadata.prompt_token_count
        token_received = response.usage_metadata.candidates_token_count
    else:
        raise RuntimeError("Api Call wasn't successfull.")
    
    if response.function_calls:
        function_results = []
        for function_call in response.function_calls:
            function_call_result = call_function(function_call=function_call, verbose=True)
            if not function_call_result.parts:
                raise Exception("Error: Function result has no parts")
            else:
                if function_call_result.parts[0].function_response == None:
                    raise Exception("Error: No response in the function call result")
                else:
                    if function_call_result.parts[0].function_response.response == None:
                        raise Exception("Error: No Actual response in the function_response.response")
                    else:
                        function_results.append(function_call_result.parts[0])
                        print(f"-> {function_call_result.parts[0].function_response.response}")
        
        contents.append(types.Content(role='user', parts=function_results))
    else:
        flag = False
        if args.verbose:
            print(f"User_prompt: {args.user_prompt}")
            print(f"token sent: {token_sent}")
            print(f"token_received: {token_received}")
            print(f"Response: \n{response.text}")
        else:
            print(f"Response: \n{response.text}")

    return flag
