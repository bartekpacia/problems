nums_str: list[str] = []
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        nums_str.append(line)


gamma_str = ""
for pos in range(12):
    zeros = 0
    ones = 0
    for j in range(len(nums_str)):
        num_str = nums_str[j]

        if num_str[pos] == "0":
            zeros += 1
        elif num_str[pos] == "1":
            ones += 1

    if zeros > ones:
        gamma_str += "0"
    else:
        gamma_str += "1"

gamma = int(gamma_str, 2)
epsilon = ~gamma & 0b111111111111

print(gamma * epsilon)


# TODO: don't operate on strings but on integers + use bitwise operations
