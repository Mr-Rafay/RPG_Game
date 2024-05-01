def is_valid_move(position):
  """Checks if a given position is within the bounds of the game map."""
  row, col = position
  return 0 <= row < 3 and 0 <= col < 3