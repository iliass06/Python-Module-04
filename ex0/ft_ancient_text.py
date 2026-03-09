if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    file = "ancient_fragment.txt"
    print(f"\nAccessing Storage Vault: {file}")
    try:
        f = open(file, "r")
        print("Connection established...")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    else:
        print("\nRECOVERED DATA:")
        data = f.read()
        f.close()
        print(data)
        print("\nData recovery complete. Storage unit disconnected.")