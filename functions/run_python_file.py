import os
import subprocess

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