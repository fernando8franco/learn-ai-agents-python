import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        is_file = os.path.isfile(target_file)
        if not is_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'

        end_with_py = file_path.endswith(".py")
        if not end_with_py:
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args:
            command.extend(args)

        result = subprocess.run(
            args=command, 
            cwd=working_dir_abs, 
            capture_output=True, 
            text=True, 
            timeout=30, 
            check=True
        )

        return format_process_output(result)

    except Exception as e:
        return f"Error: executing Python file: {e}"


def format_process_output(result: subprocess.CompletedProcess) -> str:
    parts = []

    # 1. Non-zero exit code check
    if result.returncode != 0:
        parts.append(f"Process exited with code {result.returncode}")

    # Check for output content
    has_stdout = bool(result.stdout and result.stdout.strip())
    has_stderr = bool(result.stderr and result.stderr.strip())

    # 2. No output produced
    if not has_stdout and not has_stderr:
        parts.append("No output produced")

    # 3. Include STDOUT and STDERR if present
    else:
        if has_stdout:
            parts.append(f"STDOUT:\n{result.stdout.strip()}")
        if has_stderr:
            parts.append(f"STDERR:\n{result.stderr.strip()}")

    return "\n\n".join(parts)

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python (.py) file with optional command-line arguments. Enforces a 30-second execution timeout.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The relative or target path of the Python file (.py) to execute.",
                },
                "args": {
                    "type": "array",
                    "description": "An optional list of command-line arguments to pass to the Python script.",
                    "items": {
                        "type": "string"
                    }
                },
            },
            "required": [
                "file_path"
            ]
        },
    },
}