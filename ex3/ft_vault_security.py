if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    file1 = "classified_data.txt"
    file2 = "security_protocols.txt"
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("\nSECURE EXTRACTION:")
    try:    
        with open(file1, "r") as f1:
            data1 = f1.read()
            print(data1)
    except FileNotFoundError:
        print(f"Vault '{file1}' not found.\n")
    except PermissionError:
        print(f"unable to read from '{file1}'! Access denied.\n")
    except Exception as e:
        print(f"Error: {e}")

    print("\nSECURE PRESERVATION:")
    try:
        new_protocol = "[CLASSIFIED] New security protocols archived"
        with open(file2, "w") as f2:
            f2.write(new_protocol + "\n")
            print(new_protocol)
        print("Vault automatically sealed upon completion")
    except PermissionError:
        print(f"unable to write to '{file2}'! Access denied.")
    except Exception as e:
        print(f"Error: {e}")
        
    print("\nAll vault operations completed with maximum security.")
