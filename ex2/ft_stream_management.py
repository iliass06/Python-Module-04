import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()
    id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")

    print()
    sys.stdout.write(f"[STANDARD] Archive status from {id}: {status_report}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print("\nThree-channel communication test successful.")