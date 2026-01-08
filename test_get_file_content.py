from functions.get_file_content import get_file_content

def run_tests():
    print("--- Testing lorem.txt (Truncation) ---")
    res_lorem = get_file_content("calculator", "lorem.txt")
    print(f"Length: {len(res_lorem)} characters")
    print(f"Ends with truncated message: {'truncated' in res_lorem}")

    print("\n--- Testing main.py ---")
    print(get_file_content("calculator", "main.py"))

    print("\n--- Testing pkg/calculator.py ---")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("\n--- Testing /bin/cat (Security Error) ---")
    print(get_file_content("calculator", "/bin/cat"))

    print("\n--- Testing Non-existent file (Error) ---")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    run_tests()