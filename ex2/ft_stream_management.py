import sys

if __name__ == "__main__":
    try:    
        print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
        print()
        id = input("Input Stream active. Enter archivist ID: ")
        status_report = input("Input Stream active. Enter status report: ")

        print()
        sys.stdout.write(f"[STANDARD] Archive status from {id}: {status_report}\n")
        sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
        sys.stdout.write("[STANDARD] Data transmission complete\n")
        print("\nThree-channel communication test successful.")
    
    except KeyboardInterrupt:
        sys.stderr.write("\ninput stream interrupted by user.\n")
    except EOFError:
        sys.stderr.write("\ninput stream closed unexpextedly.\n")
    except Exception as e:
        sys.stderr.write(f"\nError: {e}\n")
        