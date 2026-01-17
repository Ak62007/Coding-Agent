import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)"
            )
        }
    )
)

def get_files_info(working_directory, directory="."):
    """"""
    
    working_dir_abs = os.path.abspath(working_directory)
    target = os.path.normpath(os.path.join(working_dir_abs, directory))
    
    # Check if the target is valid
    valid_target_dir = os.path.commonpath([working_dir_abs, target]) == working_dir_abs
    
    if not valid_target_dir:
        return f'Result for {directory} directory:\n    Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target):
        return f'Result for {directory} directory:\n    Error: "{directory}" is not a directory'
    
    try:
        contents = os.listdir(target)
    except:
        return f"Result for {directory} directory:\n    Error: cannot list the contents at {directory}"
    
    info = []
    
    for content in contents:
        full_path = os.path.join(target, content)
        try:
            file_size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)
            info.append(f"{content}: file_size={file_size} bytes, is_dir={is_dir}")
        except:
            return f"Result for {directory} directory:\n    Error: Cannot get the info of the contents of the {directory}"
        
    return f"Result for {directory} directory:{"\n  -".join(info)}"
    
    # print(contents)
    
if __name__ == "__main__":
    print(get_files_info("calculator", "."))