class Monkey:
    def __init__(
        self,
        items: list[int] = [],
        op: tuple[str, str] = ("None", "None"),  # e.g (+, 2) or (*, old)
        test: int = -1,
        if_true: int = -1,
        if_false: int = -1,
    ):
        self.items = items
        self.op = op
        self.test = test
        self.if_true = if_true
        self.if_false = if_false


monkeys: list[Monkey] = []
current_monkey = Monkey()

with open("input.txt") as file:
    for l in file:
        line = l.strip()

        if not line:
            monkeys.append(current_monkey)
            current_monkey = Monkey()
        elif line.startswith("Monkey"):
            pass
        elif line.startswith("Starting items"):
            current_monkey.items = list(
                map(lambda x: int(x), line.replace(",", "").split()[2:])
            )
        elif line.startswith("Operation"):
            op = line.split()[4]
            arg = line.split()[5]
            current_monkey.op = (op, arg)
        elif line.startswith("Test"):
            current_monkey.test = int(line.split()[3])
        elif line.startswith("If true"):
            current_monkey.if_true = int(line.split()[5])
        elif line.startswith("If false"):
            current_monkey.if_false = int(line.split()[5])

    monkeys.append(current_monkey)

divisor = 1
for monkey in monkeys:
    divisor *= monkey.test

inspections = {index: 0 for index in range(len(monkeys))}


def run_round():
    for i, monkey in enumerate(monkeys):

        monkey.items = [item for item in monkey.items if item != -1]
        for j in range(len(monkey.items)):
            worry_level = monkey.items[j]

            inspections[i] += 1

            new_worry_level = -1
            if monkey.op[1] == "old":
                if monkey.op[0] == "+":
                    new_worry_level = (worry_level + worry_level) % divisor
                elif monkey.op[0] == "*":
                    new_worry_level = (worry_level * worry_level) % divisor
            else:
                if monkey.op[0] == "+":
                    new_worry_level = (worry_level + int(monkey.op[1])) % divisor
                elif monkey.op[0] == "*":
                    new_worry_level = (worry_level * int(monkey.op[1])) % divisor

            if new_worry_level % monkey.test == 0:

                monkeys[monkey.if_true].items.append(new_worry_level)

                monkey.items[j] = -1  # mark as thrown
            else:

                monkeys[monkey.if_false].items.append(new_worry_level)

                monkey.items[j] = -1  # mark as thrown


# run simulation
for i in range(10_000):
    run_round()

    for monkey in monkeys:
        monkey.items = [item for item in monkey.items if item != -1]


sorted_inspections = sorted(inspections.values(), reverse=True)
monkey_business = sorted_inspections[0] * sorted_inspections[1]
print(monkey_business)
