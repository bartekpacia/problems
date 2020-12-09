from collections import deque

PREAMBLE_LENGTH = 25

def solve_part_1(lines: list[str]) -> int:
  invalid = None
  last_segment = deque(maxlen=PREAMBLE_LENGTH)

  for i in range(PREAMBLE_LENGTH):
    last_segment.append(lines[i])

  for i in range(PREAMBLE_LENGTH, len(lines)):
    num = lines[i]

    found_match = False
    for prev_num_1 in last_segment:
      for prev_num_2 in last_segment:
        s = prev_num_1 + prev_num_2
        if s == num and prev_num_1 != prev_num_2:
          found_match = True
          break

      if found_match:
        break

    if not found_match:
      invalid = num
      return invalid

    last_segment.append(num)

  return -1 # wtf

def solve_part_2(lines: list[str], target_num: int) -> int:
  begin = 0
  end = 1

  while begin < len(lines):
    invalid_range = []
    for i in range(begin, end):
      invalid_range.append(lines[i])

    if sum(invalid_range) < target_num:
      end += 1
    elif sum(invalid_range) > target_num:
      begin += 1
    else:
      return min(invalid_range) + max(invalid_range)
  

def main():
  with open("input.txt") as f:
    lines = [int(l.strip()) for l in f.readlines()]

  invalid_num = solve_part_1(lines)
  print(f"invalid num (part 1): {invalid_num}")
  weakness = solve_part_2(lines, invalid_num)
  print(f"weakness (part 2): {weakness}")

main()