n = int(input())

banknotes = 0

hundreds, rest = divmod(n, 100)
n = rest
banknotes += hundreds

while n > 0:
    if n >= 20:
        n -= 20
    elif n >= 10:
        n -= 10
    elif n >= 5:
        n -= 5
    elif n >= 1:
        n -= 1

    banknotes += 1

print(banknotes)
