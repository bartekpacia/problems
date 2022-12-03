rock = "A"
paper = "B"
scissors = "C"

defs = {
    rock: 1,  # rock
    paper: 2,  # paper
    scissors: 3,  # scissors
}

lose = "X"
draw = "Y"
win = "Z"


def clash(enemy_shape: str, wanted_outcome: str) -> int:
    pts = 0
    my_shape: str | None

    if enemy_shape == rock:
        if wanted_outcome == lose:
            my_shape = scissors
            # no pts
        elif wanted_outcome == draw:
            my_shape = rock
            pts += 3
        elif wanted_outcome == win:
            my_shape = paper
            pts += 6
    elif enemy_shape in paper:
        if wanted_outcome == lose:
            my_shape = rock
            # no pts
        elif wanted_outcome == draw:
            my_shape = paper
            pts += 3
        elif wanted_outcome == win:
            my_shape = scissors
            pts += 6
    elif enemy_shape in scissors:
        if wanted_outcome == lose:
            my_shape = paper
            # no pts
        elif wanted_outcome == draw:
            my_shape = scissors
            pts += 3
        elif wanted_outcome == win:
            my_shape = rock
            pts += 6

    pts += defs[my_shape]
    return pts


with open("input.txt") as file:
    points = 0
    for l in file:
        line = l.strip()
        enemy_shape, outcome = line.split()
        points += clash(enemy_shape, outcome)

print(points)
