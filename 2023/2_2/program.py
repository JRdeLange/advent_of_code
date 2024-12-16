class Game:
    def __init__(self):
        self.max_dict = {
            "r": 0,
            "g": 0,
            "b": 0,
        }

    def observed(self, color, value):
        if value > self.max_dict[color]:
            self.max_dict[color] = value

    def get_power(self):
        return self.max_dict["r"] * self.max_dict["g"] * self.max_dict["b"]


input = []

with open("2_2/input.txt", "r") as f:
    input = f.read().splitlines()

sum_of_powers = 0

for line in input:
    game = Game()
    # parse the line
    line = line.split(":")
    observations = line[1].split(";")

    for observation in observations:
        observation = observation.split(",")
        for color in observation:
            n, color = color.split(" ")[1:]
            game.observed(color[0], int(n))

    sum_of_powers += game.get_power()

print(sum_of_powers)
