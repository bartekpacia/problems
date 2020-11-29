n = int(input())
text_hate = "I hate"
text_love = "I love"

text = text_hate
if n == 1:
    pass
else:
    for i in range(1, n):
        if i % 2 == 1:
            text += " that " + text_love
        else:
            text += " that " + text_hate

print(text + " it")
