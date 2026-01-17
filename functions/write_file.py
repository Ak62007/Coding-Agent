import os

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
    