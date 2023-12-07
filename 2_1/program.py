input = []

with open("2_1/input.txt", "r") as f:
    input = f.read().splitlines()

max_red = 12
max_green = 13
max_blue = 14
max_dict = {
    "red": max_red,
    "green": max_green,
    "blue": max_blue,
}

valid_games_sum = 0

for line in input:
    valid = True
    # parse the line
    line = line.split(":")
    game_id = line[0][5:]
    observations = line[1].split(";")

    for observation in observations:
        observation = observation.split(",")
        for color in observation:
            color = color.split(" ")[1:]
            if int(color[0]) > max_dict[color[1]]:
                valid = False
                break

        if not valid:
            break

    if valid:
        valid_games_sum += int(game_id)

print(valid_games_sum)
