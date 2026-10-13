import os
from functions.get_file_content import get_file_content

def main():
    # 1. Test lorem.txt truncation
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    print("\n--- Additional Test Cases ---")

    # 2. Existing file in current directory
    main_py = get_file_content("calculator", "main.py")
    print(f"main.py output:\n{main_py}\n")

    # 3. File inside subdirectory
    pkg_calc = get_file_content("calculator", "pkg/calculator.py")
    print(f"pkg/calculator.py output:\n{pkg_calc}\n")

    # 4. File outside permitted working directory (Security check)
    bin_cat = get_file_content("calculator", "/bin/cat")
    print(f"/bin/cat output:\n{bin_cat}\n")

    # 5. Non-existent file
    does_not_exist = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"pkg/does_not_exist.py output:\n{does_not_exist}")

if __name__ == "__main__":
    main()