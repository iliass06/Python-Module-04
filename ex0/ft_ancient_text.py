if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    file = "ancient_fragment.txt"
    print(f"\nAccessing Storage Vault: {file}")
    try:
        f = open(file, "r")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        data = f.read()
        f.close()
        print(data)
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except PermissionError:
        print(f"Error: unable to read from '{file}'! Access denied.")
    except Exception as e:
        print(f"Error: {e}")
