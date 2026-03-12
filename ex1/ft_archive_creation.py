if __name__ == "__main__":
    f = None
    try:
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
        file = "new_discovery.txt"
        print(f"\nInitializing new storage unit: {file}")

        f = open(file, "w")

        print("Storage unit created successfully...")
        print("\nInscribing preservation data...")

        entry1 = "[ENTRY 001] New quantum algorithm discovered"
        entry2 = "[ENTRY 002] Efficiency increased by 347%"
        entry3 = "[ENTRY 003] Archived by Data Archivist trainee"
    
        print(entry1)
        f.write(entry1 + "\n")
        print(entry2)
        f.write(entry2 + "\n")
        print(entry3)
        f.write(entry3 + "\n")

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{file}' ready for long-term preservation.")
    
    except PermissionError:
        print(f"Access denied: cannot write to '{file}'\n")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if f and not f.closed:
            f.close()
            print("\nfile closed successfully")