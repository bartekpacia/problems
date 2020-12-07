def main():
  bags = dict()
  with open("test.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

  for line in lines:
    splitties = line.split()
    container = splitties[0] + " " + splitties[1]
    # print(container)

    if "no other bags" in line:
      bags[container] = None
      continue

    contents = splitties[4:]
    start = 0
    end = 4
    while end <= len(contents):
      count = contents[start]
      print(count)

      start += 4
      end += 4

main()