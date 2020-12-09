def main():
  with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

  print(len(lines))

main()