defs = {
    "A": 1,  # rock
    "B": 2,  # paper
    "C": 3,  # scissors
    "X": 1,  # rock
    "Y": 2,  # paper
    "Z": 3,  # scissors
}

rock = ["A", "X"]
paper = ["B", "Y"]
scissors = ["C", "Z"]


def clash(enemy_shape: str, my_shape: str) -> int:
    pts = defs[my_shape]

    if enemy_shape in rock:
        if my_shape in rock:
            pts += 3
        elif my_shape in paper:
            pts += 6
        elif my_shape in scissors:
            pass
    elif enemy_shape in paper:
        if my_shape in rock:
            pass
        elif my_shape in paper:
            pts += 3
        elif my_shape in scissors:
            pts += 6
    elif enemy_shape in scissors:
        if my_shape in rock:
            pts += 6
        elif my_shape in paper:
            pass
        elif my_shape in scissors:
            pts += 3

    return pts


with open("input.txt") as file:
    points = 0
    for l in file:
        line = l.strip()
        enemy_shape, my_shape = line.split()
        points += clash(enemy_shape, my_shape)

print(points)
