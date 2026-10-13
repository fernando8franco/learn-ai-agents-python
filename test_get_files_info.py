from functions.get_files_info import get_files_info


def main():
    test_cases = [
        ("calculator", "."),
        ("calculator", "pkg"),
        ("calculator", "/bin"),
        ("calculator", "../"),
    ]

    for working_dir, target in test_cases:
        result = get_files_info(working_dir, target)
        
        # Determine the label heading based on the directory target
        label = "current directory" if target == "." else f"'{target}' directory"
        print(f'get_files_info("{working_dir}", "{target}"):')
        print(f"  Result for {label}:")
        
        # Format and print the result lines
        for line in result.split("\n"):
            print(f"    {line}" if line.startswith("Error:") else f"  {line}")
        
        print("\n")


if __name__ == "__main__":
    main()