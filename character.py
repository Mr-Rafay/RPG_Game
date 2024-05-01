# character.py

class Character:
    """Represents a game character with position and inventory."""

    def __init__(self):
        """Initializes a new character with a default position and empty inventory."""
        self.position = [0, 0]  # Starting position of the character
        self.inventory = []  # List to hold character's inventory items

    def display_inventory(self):
        """Prints the items in the character's inventory."""
        if self.inventory:
            print("Inventory:")
            for item in self.inventory:
                print(item)
        else:
            print("Your inventory is empty.")

    def pick_up_item(self, item):
        """Adds an item to the character's inventory.

        Args:
            item (str): The item to add to the inventory.
        """
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")