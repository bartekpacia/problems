def solve_part_1(lines: list[str]) -> int:
  diffs: dict[int, int] = dict()
  for i in range(len(lines)):
    if i == 0:
      prev = 0
    else:
      prev = lines[i - 1]

    current = lines[i]
    diff = current - prev

    if i == len(lines) - 1:
      diffs[3] += 1

    if not diffs.get(diff):
      diffs[diff] = 1
    else:
      diffs[diff] += 1

  return diffs[1] * diffs[3]

def main():
  with open("input.txt", "r") as f:
    lines = [int(l.strip()) for l in f.readlines()]

  lines.sort()

  part_1 = solve_part_1(lines)
  print(f"total diff (part 1): {part_1}")

    

main()