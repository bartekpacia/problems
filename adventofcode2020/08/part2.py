i = 1
acc = 0
lines: list[str] = []
executed = set()

def parse_instruction(line: str) -> (str, int):
  line = line.split()
  cmd = line[0]
  num = int(line[1])

  return cmd, num

def parse(prev, current):
  global acc, i

  if current == len(lines):
    print(f"reached last line! {acc=}, execution suspended")
    return
    
  if current in executed:
    print(f"infinite loop detected! line {current}, {acc=}, execution suspended")
    return
    # print(f"infinite loop detected! line {current}, {acc=}, trying to fix...")
    # prev_cmd, prev_num = parse_instruction(lines[prev])
    # print(f"prev_num: {prev_num:+}")
    # if prev_cmd == "nop":
    #   lines[prev] = f"jmp {prev_num:+}"
    #   parse(current, prev)

    # elif prev_cmd == "jmp":
    #   lines[prev] = f"nop {prev_num:+}"
    #   parse(current, prev)

    # else:
    #   print(f"wtf... {prev_cmd=}")
    #   return
    
    # return

  executed.add(current)
  cmd, num = parse_instruction(lines[current])

  print(f"{i} parse({current}), {cmd} {num:+} {acc=}")
  
  i += 1
  if cmd == "nop":
    parse(current, current + 1)
  elif cmd == "acc":
    acc += num
    parse(current, current + 1)
  elif cmd == "jmp":
    parse(current, current + num)

def generate_all_possible_sets():
  test_lists: list[list[str]] = []

  for j in range(len(lines)):
    line = lines[j]
    cmd, num = parse_instruction(line)
    if cmd == "nop":
      new_list: list[str] = lines.copy()
      new_list[j] = f"jmp {num:+}"
      test_lists.append(new_list)
    elif cmd == "jmp":
      new_list: list[str] = lines.copy()
      new_list[j] = f"nop {num:+}"
      test_lists.append(new_list)
    else:
      continue
    
  return test_lists

def main():
  global lines, executed, acc
  with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

  
  test_lists = generate_all_possible_sets()

  for l in test_lists:
    acc = 0
    executed = set()
    for i, elem in enumerate(l):
      if "acc" not in elem:
        print(i, elem)
    lines = l
    parse(0, 0)


main()