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
    print(f"infinite loop detected! line {current}, {acc=}, trying to fix...")
    prev_cmd, prev_num = parse_instruction(lines[prev])
    print(f"prev_num: {prev_num:+}")
    if prev_cmd == "nop":
      lines[prev] = f"jmp {prev_num:+}"
      parse(current, prev)

    elif prev_cmd == "jmp":
      lines[prev] = f"nop {prev_num:+}"
      parse(current, prev)

    else:
      print(f"wtf... {prev_cmd=}")
      return
    
    return

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


def main():
  global lines
  with open("test.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

  parse(0, 0)

main()