
names = []
with open("0022.txt") as file:
    for line in file:
        names_in_line = map(lambda s: s[1:-1], line.split(","))
        names.extend(names_in_line)

names.sort()


def name_score(name, index):
    score = 0
    for char in name:
        score += ord(char) - 64

    score *= index
    return score


total_name_score = 0
for index, name in enumerate(names):
    total_name_score += name_score(name, index + 1)


print(total_name_score)
