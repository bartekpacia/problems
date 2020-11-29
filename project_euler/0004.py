largest = 0


def is_palindrome(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    else:
        return False


for i in range(100, 1000):
    for j in range(100, 1000):
        num = i * j
        if is_palindrome(num) and num > largest:
            largest = num

print(largest)
