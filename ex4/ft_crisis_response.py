def crisis_handler(filepath: str, mode: str) -> None:
    try:
        with open(filepath, mode) as f:
            data = f.read()
            print(f"SUCCESS: Archive recovered - ''{data}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    file1 = "lost_archive.txt"
    file2 = "classified_vault.txt"
    file3 = "standard_archive.txt"

    print(f"\nCRISIS ALERT: Attempting access to '{file1}'...")
    crisis_handler(file1, "r")

    print(f"\nCRISIS ALERT: Attempting access to '{file2}'...")
    crisis_handler(file2, "r")

    print(f"\nROUTINE ACCESS: Attempting access to '{file3}'...")
    crisis_handler(file3, "r")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
