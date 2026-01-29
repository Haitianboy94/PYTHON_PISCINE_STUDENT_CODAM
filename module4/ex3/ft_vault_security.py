if __name__ == "__main__":
    """The with statement in Python simplifies resource
    management by automatically handling setup and cleanup,
    ensuring files or connections close safely even if errors occur."""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")
    with open('classified_data.txt') as file:
        print("SECURE EXTRACTION:")
        print(file.read())
    print("")
    with open('security_protocols.txt') as f:
        print("SECURE PRESERVATION:")
        print(f.read())
        print("Vault automatically sealed upon completion")
