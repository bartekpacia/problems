class Seat:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

    def __str__(self):
        return f"Seat: row: {self.row}, column: {self.column}"

    def seat_id(self) -> int:
        return self.row * 8 + self.column


def decode_pass(encoded: str) -> Seat:
    min_row = 0
    max_row = 127
    sub_row = 127
    for i in range(0, 7):
        sub_row = round(sub_row / 2)
        char = encoded[i]
        if char == "F":
            max_row -= sub_row
        elif char == "B":
            min_row += sub_row

    assert min_row == max_row

    min_column = 0
    max_column = 7
    sub_column = 7
    for i in range(7, 10):
        sub_column = round(sub_column / 2)
        char = encoded[i]
        if char == "R":
            min_column += sub_column
        elif char == "L":
            max_column -= sub_column

    assert min_column == max_column

    return Seat(max_row, max_column)


def solve_part_1(passes: list[Seat]) -> int:
    highest_seat_id = 0
    for p in passes:
        if p.seat_id() > highest_seat_id:
            highest_seat_id = p.seat_id()

    return highest_seat_id


def solve_part_2(passes: list[Seat]) -> int | None:
    passes = sorted(passes, key=lambda p: p.seat_id())

    my_seat_id = None
    i = 63
    for p in passes:
        if i != p.seat_id():
            my_seat_id = i
            break

        i += 1

    return my_seat_id


def main():
    passes: list[Seat] = []
    with open("input.txt", "r") as f:
        for line in f:
            encoded_pass = line.strip()

            decoded = decode_pass(encoded_pass)
            passes.append(decoded)

    highest_seat_id = solve_part_1(passes)
    my_seat_id = solve_part_2(passes)
    print(f"highest seat ID (part 1): {highest_seat_id}")
    print(f"my seat ID (part 2): {my_seat_id}")


main()
