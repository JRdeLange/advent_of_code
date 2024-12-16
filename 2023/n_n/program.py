input = []

with open("/input.txt", "r") as f:
    # Read in file as 2d array
    input = f.read().splitlines()

already_seen = []
total = 0



for x, line in enumerate(input):
    for y, char in enumerate(line):
        if not char.isnumeric() and char != ".":
            # for all surrounding chars
            for x2 in range(x-1, x+2):
                for y2 in range(y-1, y+2):
                    if x2 < 0 or y2 < 0 or x2 >= len(input) or y2 >= len(line):
                        continue
                    if input[x2][y2].isnumeric():
                        

