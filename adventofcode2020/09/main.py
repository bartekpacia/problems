from collections import deque

preamble_len = 5

def solve_part_1(lines: list[str]) -> int:
  invalid = None
  last_segment = deque(maxlen=preamble_len)

  for i in range(preamble_len):
    last_segment.append(lines[i])

  for i in range(preamble_len, len(lines)):
    print(f"iterating at {i}")
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
      print(f"invalid: {num}")
      invalid = num

    last_segment.append(num)

  return invalid


def main():
  with open("test.txt") as f:
    lines = [int(l.strip()) for l in f.readlines()]

  invalid_num = solve_part_1(lines)
  print(len(lines))

main()