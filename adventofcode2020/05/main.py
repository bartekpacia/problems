from typing import List

class Seat:
  def __init__(self, row: int, column: int):
    self.row = row
    self.column = column

  def __str__(self):
    return f"Seat: row: {self.row}, column: {self.column}"

  def seat_id(self):
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

def main():
  encoded_passes: List[Seat] = []
  with open("test.txt", "r") as f:
    for line in f:
      encoded_pass = line.strip()

      decoded = decode_pass(encoded_pass)
      encoded_passes.append(decoded)
  for i, p in enumerate(encoded_passes):
    print(i, str(p))

main()