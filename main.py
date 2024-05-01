from character import Character
from map import game_map, location_descriptions
from inventory import search_area
from utils import is_valid_move


def main_menu():
    """Displays the main menu and handles user selection."""
    print("1. Start Game")
    print("2. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        play_game()
    elif choice == '2':
        print("Thank you for playing!")
        quit()

def play_game():
    """Main game loop that manages the game play."""
    player = Character()  # Initialize a new player character

    while True:
        row, col = player.position
        print(location_descriptions[game_map[row][col]])

        command = input("Command (move, inventory, pick up, quit): ").lower()
        if command == "move":
            handle_movement(player)
        elif command == "inventory":
            player.display_inventory()
        elif command == "pick up":
            item = search_area(player.position)
            if item:
                player.pick_up_item(item)
            else:
                print("There is nothing to pick up here.")
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid command, please try again.")

def handle_movement(player):
    """Handles player movement based on user input."""
    direction = input("Which direction? (north, south, east, west): ").lower()
    current_row, current_col = player.position
    if direction == 'north' and is_valid_move((current_row - 1, current_col)):
        player.position[0] -= 1
    elif direction == 'south' and is_valid_move((current_row + 1, current_col)):
        player.position[0] += 1
    elif direction == 'east' and is_valid_move((current_row, current_col + 1)):
        player.position[1] += 1
    elif direction == 'west' and is_valid_move((current_row, current_col - 1)):
        player.position[1] -= 1
    else:
        print("You can't move in that direction.")

if __name__ == "__main__":
    main_menu()