import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Function to write content in a file, given a file path (relative to the working directory) and the content to write into it.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path (relative to the working directory) of the file in which content will be written.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content that will be written in the file."
            ),
        },
        required=["file_path", "content"],
    )
)

def write_file(working_directory, file_path, content):
    """"""
    
    working_dir_abs = os.path.abspath(working_directory)
    file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    
    valid_file = os.path.commonpath([working_dir_abs, file]) == working_dir_abs
    
    if not valid_file:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isdir(file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    # Make sure that all parent directories of the file_path exist.
    parent_dir = os.path.dirname(file)
    
    try:
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
    except Exception:
        return f"Error: cannot create all the parent directories of the file_path."
    
    # Writing in the file
    try:
        with open(file, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: failed to write to '{file_path}': {e}"
    