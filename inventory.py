def search_area(position):
  """Determines if there is an item to pick up based on the character's position.

  Args:
      position (list): The current position of the character.

  Returns:
      str: The name of the item found, or None if nothing is found.
  """
  items = {
      (0, 1): "Boat",
      (1, 1): "Sword",
      (2, 2): "Torch"
  }
  return items.get(tuple(position), None)