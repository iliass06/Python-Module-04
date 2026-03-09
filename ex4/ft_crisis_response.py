if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    file1 = "lost_archive.txt"
    file2 = "classified_vault.txt"
    file3 = "standard_archive.txt"

    print(f"\nCRISIS ALERT: Attempting access to '{file1}'...")
    try:
        with open(file1, "r") as f1:
    except FileNotFoundError:
