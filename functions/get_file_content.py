import os

MAX_CHARS = 10_000

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        full_target_path = os.path.abspath(os.path.join(working_directory, file_path))

        valid_target_dir = os.path.commonpath([working_dir_abs, full_target_path]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        is_file = os.path.isfile(full_target_path)
        if not is_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_target_path) as f:
            file_content_string = f.read(MAX_CHARS)

            if f.read(1):
                file_content_string += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string
        
    except Exception as e:
            return f'Error: {str(e)}'

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": (
            "Reads and returns the actual text content inside a single target file. "
            "Use this when the user asks to read, inspect, display, or analyze what is written inside a specific file. "
            "Truncates content at 10,000 characters if exceeded."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path of the specific file whose content needs to be read.",
                },
            },
            "required": [
                "file_path"
            ]
        },
    },
}