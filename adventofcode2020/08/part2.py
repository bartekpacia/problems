i = 1
acc = 0
lines: list[str] = []
executed = set()

def parse(current):
  global acc, i

  if current == len(lines):
    print(f"reached last line! {acc=}, execution suspended")
    return
    
  if current in executed:
    print(f"infinite loop detected! {acc=}, execution suspended")
    return

  executed.add(current)

  line = lines[current].split()
  cmd = line[0]
  arg = line[1]
  num = int(arg)
  
  print(f"{i} parse({current}), {cmd} {arg} {acc=}")
  
  i += 1
  if cmd == "nop":
    parse(current + 1)
  elif cmd == "acc":
    acc += num
    parse(current + 1)
  elif cmd == "jmp":
    parse(current + num)


def main():
  global lines
  with open("test.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

  parse(0)

main()