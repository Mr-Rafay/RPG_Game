# map.py

# Definition of the game map, a list of lists where each sub-list is a row of locations.
game_map = [
    ['Courtyard', 'Enchanted Forest', 'Misty Mountains'],
    ['Raging River', 'Damp Dungeon', 'Guarded Castle'],
    ['Sandy Shore', 'Mysterious Island', 'Throne Room']
]

# Mapping from locations to items that can be found there.
location_items = {
    'Enchanted Forest': 'Magic Coin',
    'Damp Dungeon': 'Rusty Key',
    'Guarded Castle': 'Silver Sword',
    'Mysterious Island': 'Golden Key'
}

# Descriptive text for each location to enhance player immersion.
location_descriptions = {
    'Courtyard': "You are standing in a quiet courtyard.",
    'Enchanted Forest': "Tall, ancient trees surround you, whispering secrets.",
    'Misty Mountains': "The path is steep and the air is thin.",
    'Raging River': "The river roars past, nearly deafening.",
    'Damp Dungeon': "It's dark and cold, and you hear distant echoes.",
    'Guarded Castle': "A formidable castle stands before you, guarded by fierce knights.",
    'Sandy Shore': "Waves gently lap at a sandy beach.",
    'Mysterious Island': "An air of mystery envelops this secluded island.",
    'Throne Room': "You've entered a grand throne room, richly decorated."
}