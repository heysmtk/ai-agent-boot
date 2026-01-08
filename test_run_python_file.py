from functions.run_python_file import run_python_file

def run_tests():
    # Test 1: Nápověda k aplikaci
    print("--- Test 1: main.py (No args) ---")
    print(run_python_file("calculator", "main.py"))

    # Test 2: Výpočet výrazu
    print("\n--- Test 2: main.py (3 + 5) ---")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    # Test 3: Spuštění testů kalkulačky
    print("\n--- Test 3: tests.py ---")
    print(run_python_file("calculator", "tests.py"))

    # Test 4: Bezpečnostní chyba (mimo adresář)
    print("\n--- Test 4: Outside path error ---")
    print(run_python_file("calculator", "../main.py"))

    # Test 5: Neexistující soubor
    print("\n--- Test 5: Nonexistent file ---")
    print(run_python_file("calculator", "nonexistent.py"))

    # Test 6: Špatný typ souboru
    print("\n--- Test 6: Not a .py file ---")
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    run_tests()