T = int(input())

for t in range(T):
    original_num = int(input())

    rests = []
    steps = 0
    divisor = 10
    last = 0
    rest_num = 0
    while True:
        last = rest_num
        rest_num = original_num % divisor
        if rest_num - last != 0:
            rests.append(rest_num - last)
            steps += 1
        divisor = divisor * 10
        if rest_num == original_num:
            print(steps)
            for i in range(len(rests)):
                if i == len(rests) - 1:
                    end = "\n"
                else:
                    end = " "
                print(rests[i], end=end)
            break
