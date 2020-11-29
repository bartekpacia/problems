line = input()
nums = [int(x) for x in line.split(" ")]
nums.sort()

a, b, c = nums

minutes_needed = 0
while a + b <= c:
    b += 1
    minutes_needed += 1

print(minutes_needed)
