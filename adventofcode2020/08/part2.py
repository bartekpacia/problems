i = 1
acc = 0
lines: list[str] = []
executed = set()

def parse(current):
  global acc, i

  stop = False
  if current == len(lines):
    print(i, f"reached last line, {acc=}, execution suspended")
    stop = True
    return
    
  if current in executed:
    print(f"INFINITE LOOP! execution suspended, {acc=}")
    return

  executed.add(current)

  line = lines[current].split()
  cmd = line[0]
  num = int(line[1])
  
  print(f"{i} parse({current}), {cmd} {line[1]} {acc=}")
  
  i += 1
  if cmd == "nop":
    parse(current + 1)
  elif cmd == "acc":
    acc += num
    if stop:
      print(f"terminated successfully, {acc=}")
      return

    parse(current + 1)
  elif cmd == "jmp":
    parse(current + num)


def main():
  global lines
  with open("test.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

  sline = lines[0].split()
  cmd = sline[0]
  num = int(sline[1])
  parse(0)

main()