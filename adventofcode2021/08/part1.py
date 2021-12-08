digits: list[str] = []
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        ds = line.split("|")[1].split()
        for digit in ds:
            digits.append(digit)


answer = 0
for digit in digits:
    l = len(digit)
    # 1 or 4 or 7 or 8
    if l == 2 or l == 4 or l == 3 or l == 7:
        answer += 1

print(answer)
