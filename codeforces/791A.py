line = input().split(" ")
limak = int(line[0])
bob = int(line[1])

i = 0
while limak <= bob:
    limak *= 3
    bob *= 2
    i += 1

print(i)
