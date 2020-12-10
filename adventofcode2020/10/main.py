def main():
  with open("test.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

  for l in lines:
    print(l)
    
main()