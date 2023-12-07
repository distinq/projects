"""
This script checks the validity of games. For each game a couple of hands are shown. The script compares these hands
with a set value inside of the bag. Whenever a value in a hand exceeds the content of the bag, the game is invalidated.
Eventually the number of valid games, are combined to generate an output
"""

import re

# Global variables
input = "day2input.txt"
totalScore = 0

# This function checks the contents of the hand with the content of the bag
def check(hand, bag):
    # Per color, the number of stones is looked up
    red = re.search("(\d+) (red)", hand)
    green = re.search("(\d+) (green)", hand)
    blue = re.search("(\d+) (blue)", hand)
    list = [red, green, blue]

    # The color variable contains the name of the color, and the number of stones
    for color in list:
        try: # Check if the color is in the bag
            color[2]
        except: # If the color is not in the bag, it continues to the next color
            continue
        if int(color[1]) > bag[color[2]]: # If the color in hand exceeds the bag, the bag is overwritten
            bag[color[2]] = int(color[1])
        else:
            continue

# This function divides each game into a gamenumber and the seperate hands within the game.
def game(line):
    # Reset the bag
    bag = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    gamesplit = line.split(':') # Split the line into gamenumber and games
    gameNo = re.search("Game (\d+)", gamesplit[0])
    gameNoInt = int(gameNo[1]) # Select the game, and the final character of the game name
    hands = gamesplit[1].split(';') # Divide the game into seperate hands

    # Each hand is checked against the bag
    for hand in hands:
        check(hand, bag)

    # The value of each colour is multiplied with the others
    output = bag["red"] * bag["green"] * bag["blue"]
    return output

# The input file is opened
with open(input) as file:
    read = file.read().split('\n')
    # For each game in the list, the game is checked and the number of the game is added to the total.
    for line in read:
        totalScore += game(line)

print(totalScore)