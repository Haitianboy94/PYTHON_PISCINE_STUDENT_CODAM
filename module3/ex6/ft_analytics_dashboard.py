if __name__ == "__main__":

    print("=== Game Analytics Dashboard ===\n")
    players = {"alice": {"score": 2300,
                         "status": True,
                         "archivements": ["first_kill", "level_10",
                                          "boss_slayer",
                                          "quest_complete", "treasure_hunter"]
                         },
               "bob": {"score": 1800,
                       "status": True,
                       "archivements": ["first_kill", "level_5",
                                        "quest_complete"]
                       },
               "charlie": {"score": 2150,
                           "status": True,
                           "archivements": ["first_kill", "level_10",
                                            "boss_slayer",
                                            "quest_complete",
                                            "treasure_hunter",
                                            "arena_champion", "speed_run"]
                           },
               "diana": {"score": 2050,
                         "status": False,
                         "archivements": ["first_kill", "level_8",
                                          "quest_complete"]
                         }
               }

    active_region = {"north": True,
                     "east": True,
                     "central": True,
                     "south": False
                     }

    new_score = []

    def list_comprehension():
        """Demonstrate list comprehensions for filtering & transforming data"""
        print("=== List Comprehension Examples ===")
        player_big_score = []
        new_score = []
        active_players = []
        for name in players:
            new_score.append(players[name]["score"] * 2)
            if players[name]["score"] > 2000:
                player_big_score.append(name)
            if players[name]["status"]:
                active_players.append(name)
        print(f"High scorers (>2000): {player_big_score}")
        print(f"Score double: {new_score}")
        print(f"Active players: {active_players}")
        print("")

    def dict_comprehension():
        """DemonstraT dic comprehensions 4 creating mappings & grouping data"""
        high_score = 0
        medium_score = 0
        low_score = 0
        player_dict = {}
        score_categories = {}
        archivements_dict = {}
        player_name = list(players.keys())
        print("=== Dict Comprehension Examples ===")
        for i in range(3):
            name = player_name[i]
            player_dict[name] = players[name]["score"]
        for player in players:
            if players[player]["score"] > 2000:
                high_score += 1
            if players[player]["score"] >= 2100:
                medium_score += 1
            if players[player]["score"] < 2000:
                low_score += 1
        for player in players:
            archivements_dict[player] = len(players[player]["archivements"])
            if len(archivements_dict) == 3:
                break
        score_categories["hight"] = high_score
        score_categories["medium"] = medium_score
        score_categories["low"] = low_score

        print(f"Player scores {player_dict}")
        print(f"Score categories: {score_categories}")
        print(f"Achievement counts: {archivements_dict}")
        print("")

    def set_comprehension():
        """Demonstrate set comprehensions for finding unique values"""
        print("=== Set Comprehension Examples ===")
        unique_player = []
        region_active = set()
        alice_archiv = set(players["alice"]["archivements"])
        bob_archiv = set(players["bob"]["archivements"])
        charlie_archiv = set(players["charlie"]["archivements"])
        diana_archiv = set(players["diana"]["archivements"])
        a_u = alice_archiv.difference(bob_archiv, charlie_archiv, diana_archiv)
        b_u = bob_archiv.difference(alice_archiv, charlie_archiv, diana_archiv)
        c_u = charlie_archiv.difference(alice_archiv, bob_archiv, diana_archiv)
        d_u = diana_archiv.difference(alice_archiv, bob_archiv, charlie_archiv)
        unique_player = (list(players.keys()))
        print(f"Unique players: {set(unique_player)}")
        all_unique = a_u.union(b_u, c_u, d_u)
        print(f"Unique achievements: {all_unique}")
        for region in active_region:
            if active_region[region]:
                region_active.add(region)
        print(f"Active regions: {region_active}")
        print("")

    def combined_analisys():
        """Process sample gaming data (scores, players, achievements, etc.)
            Show clear examples of each comprehension type in action"""
        print("=== Combined Analysis ===")
        total_player = len(players.keys())
        players_score = []
        top_perfomer = ""
        al_arc = set(players["alice"]["archivements"])
        bob_arc = set(players["bob"]["archivements"])
        char_arc = set(players["charlie"]["archivements"])
        dia_arc = set(players["diana"]["archivements"])
        tot_u_ar = len(al_arc) + len(bob_arc) + len(char_arc) + len(dia_arc)
        print(f"Total players: {total_player}")
        print(f"Total unique achievements: {tot_u_ar}")
        for player in players:
            players_score.append(players[player]["score"])
            if players[player]["score"] == max(players_score):
                top_perfomer += player
        average_score = sum(players_score) / len(players_score)
        print(f"Average score: {average_score}")
        print(f"Top performer: {top_perfomer} ({max(players_score)} points,"
              f"{len(players[top_perfomer]["archivements"])} archivements)")

    list_comprehension()
    dict_comprehension()
    set_comprehension()
    combined_analisys()
