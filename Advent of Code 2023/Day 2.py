"""
This script checks the validity of games. For each game a couple of hands are shown. The script compares these hands
with a set value inside of the bag. Whenever a value in a hand exceeds the content of the bag, the game is invalidated.
Eventually the number of valid games, are combined to generate an output
"""

import re

# Global variables
input = "day2input.txt"
totalScore = 0

# Starting off with a dictionary of the bag
bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}
# This function checks the contents of the hand with the content of the bag
def check(hand):
    # Per color, the number of stones is looked up
    red = re.search("(\d+) (red)", hand)
    green = re.search("(\d+) (green)", hand)
    blue = re.search("(\d+) (blue)", hand)
    list = [red, green, blue]

    # The color variable contains the name of the color, and the number of stones
    correct = True
    for color in list:
        try: # Check if the color is in the bag
            color[2]
        except: # If the color is not in the bag, it continues to the next color
            continue

        if int(color[1]) > bag[color[2]]: # Check to see if the value in hand does not exceed bag
            correct = False
        else:
            continue
    return correct

# This function divides each game into a gamenumber and the seperate hands within the game.
def game(line):
    fail = 0
    # Check what game it is, split the string into the gamenumber and games
    gamesplit = line.split(':')
    gameNo = re.search("Game (\d+)", gamesplit[0])
    gameNoInt = int(gameNo[1]) # Select the game, and the final character of the game name
    hands = gamesplit[1].split(';') # Divide the game into seperate hands

    # The check is performed per hand
    for hand in hands:
        if check(hand):
            fail += 0
        else:
            fail += 1
    # Decide what the result of the game is
    if fail == 0:
        return gameNoInt
    else:
        return 0


# The input file is opened
with open(input) as file:
    read = file.read().split('\n')
    # For each game in the list, the game is checked and the number of the game is added to the total.
    for line in read:
        totalScore += game(line)

print(totalScore)