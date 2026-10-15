import os
from functions.write_file import write_file  # Adjust import based on your project structure


def test_write_file():
    print("Testing write_file...\n")

    # Test Case 1: Valid relative path file write
    res1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Test 1 Result: {res1}")

    # Test Case 2: Valid relative path with subdirectory
    res2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Test 2 Result: {res2}")

    # Test Case 3: Path traversal / outside directory check
    res3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Test 3 Result: {res3}")


if __name__ == "__main__":
    test_write_file()