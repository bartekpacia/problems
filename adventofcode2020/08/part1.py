acc = 0
lines: list[str] = []
executed = set()

def parse(current):
  print(f"parse({current=})")
  global acc

  if current in executed:
    print(f"INFINITE LOOP! execution suspended, {acc=}")
    return

  executed.add(current)

  line = lines[current].split()
  cmd = line[0]
  num = int(line[1])
  print(f"parse({current})")
  if cmd == "nop":
    parse(current + 1)
  elif cmd == "acc":
    acc += num
    parse(current + 1)
  elif cmd == "jmp":
    parse(current + num)


def main():
  global lines
  with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

  sline = lines[0].split()
  cmd = sline[0]
  num = int(sline[1])
  parse(0)

main()