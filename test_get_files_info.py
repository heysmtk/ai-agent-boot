from functions.get_files_info import get_files_info

def run_tests():
    print("get_files_info('calculator', '.'):")
    print(f"  Result for current directory:\n{get_files_info('calculator', '.')}")
    print("-" * 30)

    print("get_files_info('calculator', 'pkg'):")
    print(f"  Result for 'pkg' directory:\n{get_files_info('calculator', 'pkg')}")
    print("-" * 30)

    print("get_files_info('calculator', '/bin'):")
    print(f"  Result for '/bin' directory:\n    {get_files_info('calculator', '/bin')}")
    print("-" * 30)

    print("get_files_info('calculator', '../'):")
    print(f"  Result for '../' directory:\n    {get_files_info('calculator', '../')}")

if __name__ == "__main__":
    run_tests()