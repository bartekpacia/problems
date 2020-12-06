def solve_part_1(lines: list[str]) -> int:
  sum_of_yesses = 0
  current_yes_answers = set()
  for line in lines:
    if line != "":
      for char in line:
        current_yes_answers.add(char)
    else:
      sum_of_yesses += len(current_yes_answers)
      current_yes_answers = set()

  # Add set made from the last line, which is omitted in the loop above
  sum_of_yesses += len(current_yes_answers)
  
  return sum_of_yesses

def solve_part_2(lines: list[str]) -> int:
  all_groups_yes_answers: list[dict[str, int]] = list()
  all_groups_line_count: list[int] = list()
  current_yes_answers = dict()
  current_line_count = 0
  for line in lines:
    if line != "":
      current_line_count += 1
      for char in line:
        if not current_yes_answers.get(char):
          current_yes_answers[char] = 1
        else:
          current_yes_answers[char] += 1
    else:
      all_groups_yes_answers.append(current_yes_answers)
      all_groups_line_count.append(current_line_count)
      current_yes_answers = dict()
      current_line_count = 0

  # don't forget about the last group!
  all_groups_yes_answers.append(current_yes_answers)
  all_groups_line_count.append(current_line_count)

  # iterate over alphabet  
  sum_of_yesses = 0
  for i in range(len(all_groups_yes_answers)):
    group = all_groups_yes_answers[i]
    group_line_count = all_groups_line_count[i]

    print(f"num: {i + 1}, lines: {group_line_count} group: {group}")
    for char, occurrences in group.items():
      if occurrences == group_line_count:
        sum_of_yesses += 1 

  return sum_of_yesses

def main():
  with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

  sum_of_yesses_1 = solve_part_1(lines)
  sum_of_yesses_2 = solve_part_2(lines)
  print(f"sum of yesses (part 1): {sum_of_yesses_1}")
  print(f"sum of yesses (part 2): {sum_of_yesses_2}")
  
  
main()
