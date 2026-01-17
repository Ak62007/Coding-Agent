import os
from google.genai import types
from config import MAX_CHARS

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read contents of a file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path of the file to get the contents from, relative to the working directory (default is the working directory itself)",
            )
        },
        required=["file_path"],
    )
)

def get_file_content(working_directory, file_path):
    """"""
    
    working_dir_abs = os.path.abspath(working_directory)
    target = os.path.normpath(os.path.join(working_dir_abs, file_path))
    
    # cheacking the validity
    valid_target = os.path.commonpath([working_dir_abs, target]) == working_dir_abs
    
    if not valid_target:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    # Reading the file
    try:
        with open(target, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except:
        return f"Error: Cannot read {file_path}"
    
    return file_content_string        
    
    