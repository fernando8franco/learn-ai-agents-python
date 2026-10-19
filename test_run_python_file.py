from functions.run_python_file import run_python_file

def test_run_python_file():
    print("--- Test 1: Usage instructions ---")
    res1 = run_python_file("calculator", "main.py")
    print(res1)
    print("\n" + "=" * 50 + "\n")

    print("--- Test 2: Execute calculation ('3 + 5') ---")
    res2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(res2)
    print("\n" + "=" * 50 + "\n")

    print("--- Test 3: Run calculator tests ---")
    res3 = run_python_file("calculator", "tests.py")
    print(res3)
    print("\n" + "=" * 50 + "\n")

    print("--- Test 4: Path traversal attempt ('../main.py') ---")
    res4 = run_python_file("calculator", "../main.py")
    print(res4)
    print("\n" + "=" * 50 + "\n")

    print("--- Test 5: Nonexistent Python file ('nonexistent.py') ---")
    res5 = run_python_file("calculator", "nonexistent.py")
    print(res5)
    print("\n" + "=" * 50 + "\n")

    print("--- Test 6: Non-python file ('lorem.txt') ---")
    res6 = run_python_file("calculator", "lorem.txt")
    print(res6)
    print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    test_run_python_file()