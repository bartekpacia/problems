with open("sample.txt") as file:
    stack: list[list[str]] = []

    layout: list[str] = []
    for l in file:
        line = l.strip()
        if not line:
            break
            
        layout.append(line)

    print(layout[-1])


print(''.join(layout))
