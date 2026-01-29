if __name__ == "__main__":
    """Manage player inventories (like your personal treasure chest!)
• Track item details: quantities, types, values (is it worth keeping?)
• Calculate total inventory value (how rich are you?)
• Organize items by categories (weapons, potions, armor, etc.)
• Generate cool inventory reports (show off your collection!)"""
    print("=== Player Inventory System ===")
    print("")
    alice_dict = {"sword": {"amount": 1, "type": "weapon",
                            "rarety": "rare", "value": 500},
                  "potion": {"amount": 5, "type": "consumable",
                             "rarety": "common", "value": 50},
                  "shield": {"amount": 1, "type": "armor",
                             "rarety": "uncommon", "value": 200}
                  }

    bob_dict = dict()

    # FOR SWORD
    al_tp = alice_dict["sword"]["type"]
    al_r = alice_dict["sword"]["rarety"]
    al_t = alice_dict["sword"]["amount"]*alice_dict["sword"]["value"]
    al_am = alice_dict["sword"]["amount"]
    al_v = alice_dict["sword"]["value"]

    # FOR POTION
    al_po = alice_dict["potion"]["type"]
    al_pos = alice_dict["potion"]["rarety"]
    al_pst = alice_dict["potion"]["amount"]*alice_dict["potion"]["value"]
    al_pi = alice_dict["potion"]["amount"]
    al_ptt = alice_dict["potion"]["value"]

    # FOR SHIELD
    al_sh = alice_dict["shield"]["type"]
    al_si = alice_dict["shield"]["rarety"]
    al_sd = alice_dict["shield"]["amount"]*alice_dict["shield"]["value"]
    al_sl = alice_dict["shield"]["amount"]
    al_sv = alice_dict["shield"]["value"]

    # TOTAL VALUE FOR ALICE
    total_all_value = al_t + al_pst + al_sd

    print("=== Alice's Inventory ===")
    alice_key = list(alice_dict.keys())
    alice_value = list(alice_dict.values())

    print(f"{alice_key[0]} ({al_tp}, {al_r}): {al_am}x @ {al_v}, "
          f"gold each = {al_t} gold")
    print(f"{alice_key[1]} ({al_po}, {al_pos}): {al_pi}x @ {al_ptt}, "
          f"gold each = {al_pst} gold")
    print(f"{alice_key[2]} ({al_sh}, {al_si}): {al_sl}x @ {al_sv}, "
          f"gold each = {al_sd} gold\n")
    print(f"Inventory value: {total_all_value} gold")
    print(f"Item count: {al_am + al_pi + al_sl} items")
    print(f"Categories: weapon({al_am}), consumable({al_pi}), armor({al_sl})")
    print("")

    # TRANSACTION FROM ALICE TO BOB
    transaction = 2
    if al_pi >= transaction:
        print(f"=== Transaction: Alice gives Bob {transaction} potions ===")
        print("Transaction successful!\n")

        print("=== Updated Inventories ===")
        alice_dict["potion"]["amount"] -= transaction
        bob_dict["potion"] = {"amount": 0}
        bob_dict["potion"]["amount"] += transaction
        print(f"Alice potions: {alice_dict["potion"]["amount"]}")
        print(f"Bob potion: {bob_dict["potion"]["amount"]}\n")
    else:
        print("Not enouth potion to share!")

    print("=== Inventory Analytics ===")
    al_tn = alice_dict["sword"]["amount"]*alice_dict["sword"]["value"]
    al_pstn = alice_dict["potion"]["amount"]*alice_dict["potion"]["value"]
    al_sdn = alice_dict["shield"]["amount"]*alice_dict["shield"]["value"]
    new_total_value_Alice = al_tn + al_pstn + al_sdn
    nal_am = alice_dict["sword"]["amount"]
    nal_pi = alice_dict["potion"]["amount"]
    nal_sl = alice_dict["shield"]["amount"]

    alice_items = nal_am + nal_pi + nal_sl

    print(f"Most valuable player: Alice {new_total_value_Alice} gold")
    print(f"Most items: Alice ({alice_items} items)")
    print(f"Rarest items: {alice_key[0]}, magics_ring")
