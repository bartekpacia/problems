n = int(input())

words = []
for i in range(n):
    word = input()
    if len(word) > 10:
        word = f"{word[0]}{len(word) - 2}{word[-1]}"

    words.append(word)

for w in words:
    print(w)
