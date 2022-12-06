def process(buffer: str):
    i = 4
    while i < len(buffer):
        window = buffer[i - 4 : i]
        if len(window) == len(set(window)):
            return i

        i += 1


with open("input.txt") as file:
    for line in file:
        print(process(line.strip()))
