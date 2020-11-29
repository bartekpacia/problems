def digit_to_text(digit):
    if digit == 1:
        return "one"
    elif digit == 2:
        return "two"
    elif digit == 3:
        return "three"
    elif digit == 4:
        return "four"
    elif digit == 5:
        return "five"
    elif digit == 6:
        return "six"
    elif digit == 7:
        return "seven"
    elif digit == 8:
        return "eight"
    elif digit == 9:
        return "nine"
    else:
        return None


def teen_to_text(digit):
    if digit == 1:
        return "ten"
    elif digit == 11:
        return "eleven"
    elif digit == 12:
        return "twelve"
    elif digit == 13:
        return "thirteen"
    elif digit == 14:
        return "fourteen"
    elif digit == 15:
        return "fifteen"
    elif digit == 16:
        return "sixteen"
    elif digit == 17:
        return "seventeen"
    elif digit == 18:
        return "eighteen"
    elif digit == 19:
        return "nineteen"
    else:
        return None


def convert_to_text(num):
    text = ""

    hundreds = num // 100
    tens = num // 10

    if hundreds:
        text += digit_to_text(hundreds) + " hundred"

    if tens:
        if tens == 1:
            if num > 100:
                real_ten = real_ten - (hundreds * 100)
            else:
                real_ten = num
            text += teen_to_text(real_ten)

    return text


print(convert_to_text(1))
print(convert_to_text(11))
print(convert_to_text(16))
print(convert_to_text(22))
