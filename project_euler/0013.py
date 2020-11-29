sum = 0

i = 0
with open("data_0013.txt") as f:
    while True:
        line = f.readline()

        if not line:
            print("End of file")
            break

        line = line.strip("\n")

        num = int(line)
        sum += num
        print(f"index {i}: line '{line}'.")
        i += 1

sum_str = str(sum)
first_ten = sum_str[0:10]

print(f"i: {i}, sum: {sum}, first_ten: {first_ten}")
