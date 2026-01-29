if __name__ == "__main__":
    """Track unique achievements (no "First Kill" counted twice!)
• Find achievements shared by multiple players (the "common ground")
• Spot the ultra-rare achievements (bragging rights material!)
• See who’s missing what achievements (gotta catch ’em all!)
• Build player communities based on shared accomplishments"""
    print("=== Achievement Tracker System ===\n")
    alice_achi = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob_achi = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie_achi = {'level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist'}

    print(f"Player alice archivements: {alice_achi}")
    print(f"Player bob archivements: {bob_achi}")
    print(f"Player charlie archivements: {charlie_achi}\n")

    """THE UNION() IS USED TO SAVE ALL ELEMENT FROM EACH SET IN A VARIABLE
    CALLED ALL_UNIQUE_ACHI, (DUPLICATE REMOVED AUTOMATICALLY)"""
    print("=== Achievement Analytics ===")
    all_unique_achi = alice_achi.union(bob_achi).union(charlie_achi)
    print(f"All unique archivements: {all_unique_achi}")
    print(f"Total unique archivements: {len(all_unique_achi)}\n")

    """THE INTERSECTION() IS USED TO SAVE THE COMMON ELEMENT IN A VARIABLE
    CALLED (COMMON TO ALL)"""
    common_to_al = alice_achi.intersection(bob_achi).intersection(charlie_achi)
    print(f"Common to all players: {common_to_al}")

    """THE DIFFERENCE() IS USED TO SAVE THE ELEMENT THAT BELONG TO ONLY ONE
    SET, (ONLY ONE SET HAVE)"""
    alice_rare = alice_achi.difference(bob_achi, charlie_achi)
    bob_rare = bob_achi.difference(alice_achi, charlie_achi)
    charlie_rare = charlie_achi.difference(alice_achi, bob_achi)

    rare_achievements = alice_rare.union(bob_rare).union(charlie_rare)
    print(f"Rare achievements (1 player): {rare_achievements}\n")

    alice_vs_bob = alice_achi.intersection(bob_achi)
    print(f"Alice vs Bob common: {alice_vs_bob}")
    alice_unique = alice_achi.difference(bob_achi)
    print(f"Alice unique: {alice_unique}")
    bob_unique = bob_achi.difference(alice_achi)
    print(f"Bob unique: {bob_unique}")
