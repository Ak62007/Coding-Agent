import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Given a file path of python file (relative to the working directory), This function runs python script and gives the results",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path (relative to the working directory) of the python file that should be ran.",
            ),
            
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of command-line arguments to pass to the script.",
                items=types.Schema(type=types.Type.STRING)
            )
        },
        required=["file_path"]
    )
)

def run_python_file(working_directory, file_path, args=None):
    """"""
    
    working_dir_abs = os.path.abspath(working_directory)
    file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    
    valid_file = os.path.commonpath([working_dir_abs, file]) == working_dir_abs
    
    if not valid_file:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(file):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if not file_path[-3:] == ".py":
        return f'Error: "{file_path}" is not a Python file'
    
    # building the command
    command = ["python", file]
    if args:
        command.extend(args)
        
    # running the subprocess
    try:
        result = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30
        )
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    # Building the output
    output = ""
    if result.returncode != 0:
        output += f"Process exited with code {result.returncode}"
    if not result.stdout and not result.stderr:
        output += "No output produced"
    else:
        if result.stdout:
            output += f"STDOUT: {result.stdout}"
        if result.stderr:
            output += f"STDERR: {result.stderr}"
            
    return output