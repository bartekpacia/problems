def solve_part_1(lines: list[str]) -> int:
  sum_of_yesses = 0
  current_yes_answers = set()
  for line in lines:
    # print(repr(line))
    if line != "":
      for char in line:
        current_yes_answers.add(char)
    else:
      sum_of_yesses += len(current_yes_answers)
      current_yes_answers = set()

  # Add set made from the last line, which is omitted in the loop above
  sum_of_yesses += len(current_yes_answers)
  
  return sum_of_yesses

def main():
  with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

  sum_of_yesses = solve_part_1(lines)
  print(f"sum of yesses (part 1): {sum_of_yesses}")

  
  
main()
