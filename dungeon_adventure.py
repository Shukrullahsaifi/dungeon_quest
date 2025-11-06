import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.
        """
        name = input("Enter your name: ").strip()
        if not name:
            name = "Adventurer"
        player = {
            "name": name,
            "health": 10,
            "inventory": []
        }
        print(f"Welcome, {player['name']}! You start with {player['health']} health.")
        return player


    def create_treasures():
        """
        Creates and returns a dictionary of treasures and their values.
        Values are randomized a bit to make the game different each play.
        """
        treasures = {
            "gold coin": random.randint(3, 8),
            "ruby": random.randint(8, 12),
            "ancient scroll": random.randint(6, 10),
            "emerald": random.randint(7, 11),
            "silver ring": random.randint(2, 6),
            "mystic amulet": random.randint(9, 14),
            "small gem": random.randint(1, 5)
        }
        return treasures
    


    def display_options(room_number):
        """
        Displays available options for the player in the current room.
        """
        print("\n" + "-" * 40)
        print(f"You are in room {room_number}.")
        print("What would you like to do?")
        print("1. Search for treasure")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit the game")


    def search_room(player, treasures):
        """
        Simulates searching the current room.
        Randomly chooses 'treasure' or 'trap'.
        """
        outcome = random.choice(["treasure", "trap"])
        if outcome == "treasure":
            # choose a random treasure name
            treasure_name = random.choice(list(treasures.keys()))
            player["inventory"].append(treasure_name)
            value = treasures[treasure_name]
            print(f"\nYou searched the room and found a '{treasure_name}' worth {value} points!")
        else:
            # trap: deduct health (use a small random damage, e.g., 2-4)
            damage = random.randint(2, 4)
            player["health"] -= damage
            print(f"\nOh no! You triggered a trap and lost {damage} health.")
            if player["health"] <= 0:
                print("Your health has dropped to 0 or below!")


    def check_status(player):
        """
        Displays the player's current health and inventory.
        """
        print("\n-- Player Status --")
        print(f"Health: {player['health']}")

        if player["inventory"]:
            print("Inventory: " + ", ".join(player["inventory"]))
        else:
            print("Inventory: You have no items yet.")

    print("-- End Status --")


    def end_game(player, treasures):
        """
        Ends the game and displays a summary including total treasure value.
        """
        total_value = 0
        for item in player["inventory"]:
            # If item not in treasures dict (defensive), treat value 0
            total_value += treasures.get(item, 0)

        print("\n" + "=" * 40)
        print("Game Over! Final summary:")
        print(f"Player: {player['name']}")
        print(f"Final Health: {max(player['health'], 0)}")
        if player["inventory"]:
            print("Final Inventory: " + ", ".join(player["inventory"]))
        else:
            print("Final Inventory: (none)")
        print(f"Total treasure value: {total_value}")
        print("Thanks for playing!")
        print("=" * 40)


    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.
        """
        # There are 5 rooms
        for room_number in range(1, 6):
            print(f"\nEntering room {room_number}...")
            # Each room allows multiple actions until player moves forward or quits or dies
            while True:
                # If player's health is 0 or less, end the game early
                if player["health"] <= 0:
                    print("\nYou don't have enough health to continue.")
                    end_game(player, treasures)
                    return

                display_options(room_number)
                choice = input("Enter choice (1-4): ").strip()

                if choice == "1":
                    search_room(player, treasures)
                    # After searching, check health and continue in same room unless dead
                    if player["health"] <= 0:
                        print("You have died from your injuries.")
                        end_game(player, treasures)
                        return
                    # continue in the current room after search
                elif choice == "2":
                    print("You move to the next room.")
                    # break inner loop to proceed to next room
                    break
                elif choice == "3":
                    check_status(player)
                elif choice == "4":
                    print("You chose to quit the game.")
                    end_game(player, treasures)
                    return
                else:
                    print("Invalid choice. Please type 1, 2, 3, or 4.")

        # Player finished all rooms
        print("\nYou have explored all rooms!")
        end_game(player, treasures)


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
