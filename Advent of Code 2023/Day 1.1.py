# Variables
source = "day1input.txt"
total = 0

# Function to perform the calculation
def calculation(code):
    l = len(code)
    first = 0
    second = 0
    # For the length of the string inputed, the code will iterate through the letters to check for an integer
    # When the integer is found, the loop breaks and the number, as string is assigned to the first variable
    for n in range(l):
        try:
            int(code[n])
            first = code[n]
            break
        except:
            continue

    # The same logic is used, but the iteration is in reverse
    for n in reversed(range(l)):
        try:
            int(code[n])
            second = code[n]
            break
        except:
            continue
    # The two found numbers are combined and converted to integers
    return(int(first+second))

# Open the file
with open(source, 'r') as file:
    data = file.read().split('\n')

    # Iterate throught the file to check each line of code
    for line in data:
        total += calculation(line)

print(total)