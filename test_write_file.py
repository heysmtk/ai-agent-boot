from functions.write_file import write_file

def run_tests():
    print("Test 1: Writing to lorem.txt")
    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"  Result: {result1}")

    print("\nTest 2: Writing to pkg/morelorem.txt")
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"  Result: {result2}")

    print("\nTest 3: Writing to /tmp/temp.txt")
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"  Result: {result3}")

if __name__ == "__main__":
    run_tests()