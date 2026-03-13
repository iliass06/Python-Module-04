# if __name__ == "__main__":
#     print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
#     file1 = "lost_archive.txt"
#     file2 = "classified_vault.txt"
#     file3 = "standard_archive.txt"

#     print(f"\nCRISIS ALERT: Attempting access to '{file1}'...")
#     try:
#         with open(file1, "r") as f1:
#             data = f1.read()
#     except FileNotFoundError:
#         print("RESPONSE: Archive not found in storage matrix")
#         print("STATUS: Crisis handled, system stable")

#     print(f"\nCRISIS ALERT: Attempting access to '{file2}'...")
#     try:
#         with open(file2, "r") as f2:
#             data2 = f2.read()
#             print(f"SUCCESS: {data2}")
#     except FileNotFoundError:
#         print("RESPONSE: Archive not found in storage matrix")
#         print("STATUS: Crisis handled, system stable")
#     except PermissionError:
#         print("RESPONSE: Security protocols deny access")
#         print("STATUS: Crisis handled, security maintained")
#     except Exception as e:
#         print(f"Error: {e}")

#     print(f"\nROUTINE ACCESS: Attempting access to '{file3}'...")
#     try:
#         with open(file3, "r") as f3:
#             data3 = f3.read()from typing import Any

# # VOICI LA FONCTION EXIGÉE PAR LE SUJET
# def crisis_handler(filepath: str, mode: str) -> None:
#     try:
#         with open(filepath, mode) as f:
#             data = f.read()
#             print(f"SUCCESS: Archive recovered - ''{data}''")
#             print("STATUS: Normal operations resumed")
#     except FileNotFoundError:
#         print("RESPONSE: Archive not found in storage matrix")
#         print("STATUS: Crisis handled, system stable")
#     except PermissionError:
#         print("RESPONSE: Security protocols deny access")
#         print("STATUS: Crisis handled, security maintained")
#     except Exception as e:
#         print(f"Error: {e}")

# def main() -> None:
#     print("=== CYBERprint ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    
#     file1 = "lost_archive.txt"
#     file2 = "classified_vault.txt"
#     file3 = "standard_archive.txt"

#     print(f"\nCRISIS ALERT: Attempting access to '{file1}'...")
#     crisis_handler(file1, "r")

#     print(f"\nCRISIS ALERT: Attempting access to '{file2}'...")
#     crisis_handler(file2, "r")
# print
#     print(f"\nROUTINE ACCESS: Attempting access to '{file3}'...")
#     crisis_handler(file3, "r")

#     print("\nAll crisis scenarios handled successfully. Archives secure.")

# if __name__ == "__main__":
#     main()
#         print(f"SUCCESS: Archive recovered - ''{data3}''")
#         print("STATUS: Normal operations resumed")
#     except FileNotFoundError:
#         print(f"'{file3}' not found")
#     except PermissionError:
#         print(f"unable to read from '{file3}'! Access denied.")
#     except Exception as e:
#         print(f"Error: {e}")

#     print("\nAll crisis scenarios handled successfully. Archives secure.")


import sys

sys.stdout.write("ID: ") # On doit afficher le message manuellement
sys.stdout.flush()       # On force l'affichage (car pas de \n)

line = sys.stdin.readline() # Lit une ligne entière
user_id = line.strip()      # .strip() est CRUCIAL pour enlever le \n à la fin

print(user_id)