# open and read input.txt
input = []
sum = 0

with open("1_1/input.txt", "r") as f:
    input = f.read().splitlines()

for line in input:
    # obtain only the numeric characters
    numbers = []
    for char in line:
        if char.isdigit():
            numbers.append(char)

    sum += int(numbers[0] + numbers[-1])

print(sum)
