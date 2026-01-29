if __name__ == "__main__":
    """Mixed with all"""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    try:
        with open('lost_archive.txt') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access "
              f"to '{'lost_archive.txt'}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
        print("")

    try:
        with open('classified_vault.txt') as file:
            print(f"SUCCESS: Archive recovered - {file.read()}")
    except (PermissionError, FileNotFoundError):
        print(f"CRISIS ALERT: Attempting access to "
              f"'{'classified_vault.txt'}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
        print("")

    try:
        with open('standard_archive.txt') as file:
            print(f"ROUTINE ACCESS: Attempting access to "
                  f"'{'standard_archive.txt'}'...")
            print(f"SUCCESS: Archive recovered - {file.read()}")
            print("STATUS: Normal operations resumed")
            print("")
    except (PermissionError, FileNotFoundError):
        print("CRISIS ALERT: Attempting access to 'standard_archive.txt'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    print("All crisis scenarios handled successfully. Archives secure.")
