from functions.get_files_info import get_files_info


def main():
    test_cases = [
        ("calculator", "."),
        ("calculator", "/bin"),
        ("calculator", "../"),
        ("calculator", "main.py"),
    ]

    for i, (working_dir, target) in enumerate(test_cases, start=1):
        result = get_files_info(working_dir, target)
        print(f"{i}. get_files_info('{working_dir}', '{target}'): {result}")


if __name__ == "__main__":
    main()