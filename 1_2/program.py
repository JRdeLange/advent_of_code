def find_all(substring, string):
    """
    Find all occurences of a substring in a string
    """
    positions = []
    for i in range(len(string)):
        if string[i] == substring[0]:
            if string[i : i + len(substring)] == substring:
                positions.append(i)
    return positions


# open and read input.txt
input = []
sum = 0

word_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

with open("1_2/input.txt", "r") as f:
    input = f.read().splitlines()

for line in input:
    # obtain only the numeric characters
    numbers = []
    indices = []
    for key in word_dict.keys():
        positions = find_all(key, line)
        for pos in positions:
            numbers.append(word_dict[key])
            indices.append(pos)

    # sort the numbers by their index
    numbers = [x for _, x in sorted(zip(indices, numbers))]

    sum += int(numbers[0] + numbers[-1])

print(sum)
