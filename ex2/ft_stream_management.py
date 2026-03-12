import sys

if __name__ == "__main__":
    try:    
        print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
        print()
        id = input("Input Stream active. Enter archivist ID: ")
        status_report = input("Input Stream active. Enter status report: ")

        print()
        print(f"[STANDARD] Archive status from {id}: {status_report}")
        print("[ALERT] System diagnostic: Communication channels verified", file=sys.stderr)
        print("[STANDARD] Data transmission complete")
        print("\nThree-channel communication test successful.")
    
    except KeyboardInterrupt:
          print("\nInput stream interrupted by user.", file=sys.stderr)
    except EOFError:
          print("\nInput stream closed unexpectedly.", file=sys.stderr)
    except Exception as e:
          print(f"\nError: {e}", file=sys.stderr)
        