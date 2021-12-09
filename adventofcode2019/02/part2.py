with open("input.txt") as f:
    program = [int(l) for l in f.readline().split(",")]


for noun in range(100):
    for verb in range(100):
        memory = program.copy()

        memory[1] = noun
        memory[2] = verb

        ip = 0  # instruction pointer
        while True:
            opcode = memory[ip]
            print(f"opcode {opcode} at instruction pointer {ip}")
            if opcode == 1:
                num1 = memory[memory[ip + 1]]
                num2 = memory[memory[ip + 2]]
                memory[memory[ip + 3]] = num1 + num2
            elif opcode == 2:
                num1 = memory[memory[ip + 1]]
                num2 = memory[memory[ip + 2]]
                memory[memory[ip + 3]] = num1 * num2
            else:  # opcode = 99
                break

            ip += 4

        if memory[0] == 19690720:
            print(100 * noun + verb)
            exit(0)
