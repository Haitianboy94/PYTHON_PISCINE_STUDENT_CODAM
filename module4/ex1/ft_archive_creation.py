if __name__ == "__main__":
    """Files in python"""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {'new_discovery.txt'}")
    print("Storage unit created successfully...")
    print("")
    print("Inscribing preservation data...")
    new_file = open('new_discovery.txt', 'w')
    new_file.write("{[}ENTRY 001{]} New quantum algorithm discovered\n"
                   "{[}ENTRY 002{]} Efficiency increased by 347%\n"
                   "{[}ENTRY 003{]} Archived by Data Archivist trainee\n")
    new_file.close()
    new_file = open('new_discovery.txt', 'r')
    print(new_file.read())
    new_file.close()

    print("Data recovery complete. Storage unit disconnected.")
