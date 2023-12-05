"""
This script checks the validity of games. For each game a couple of hands are shown. The script compares these hands
with a set value inside of the bag. Whenever a value in a hand exceeds the content of the bag, the game is invalidated.
Eventually the number of valid games, are combined to generate an output
"""

import re

# Global variables
input = "day2input.txt"

# Starting off with a dictionary of the bag
bag = {
    "Red": 12,
    "Green": 13,
    "Blue": 14
}

def game(line):
    # Check what game it is
    m = re.search("Game (\d+)", line)
    print(m.group(1))

with open(input) as file:
    read = file.read().split('\n')
    for line in read:
        print(line)
        # game(line)