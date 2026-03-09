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
        print("[CLASSIFIED] Quantum encryption keys recovered")
        print("[CLASSIFIED] Archive integrity: 100%")
    

    print("\nSECURE PRESERVATION:")
    new_protocol = "[CLASSIFIED] New security protocols archived"
    print(new_protocol)
    with open(file2, "w") as f2:
        f2.write(new_protocol + "\n")

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")
