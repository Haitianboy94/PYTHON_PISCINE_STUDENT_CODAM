if __name__ == "__main__":
    """Files in python"""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {'ancient_fragment.txt'}")
    print("Connection established...")
    print("")
    print("RECOVERED DATA:")
    my_file = open('ancient_fragment.txt', 'r')
    file_content = my_file.read()
    print(file_content)
    my_file.close()
    print("")
    print("Data recovery complete. Storage unit disconnected")
