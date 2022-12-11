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

with open("sample.txt") as file:
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


# for i, monkey in enumerate(monkeys):
#     print(f'Monkey {i}')
#     print(f'  Starting items: {monkey.items}')
#     print(f'  Operation: new = old {monkey.op[0]} {monkey.op[1]}')
#     print(f'  Test: divisible by {monkey.test}')
#     print(f'    If true: throw to monkey {monkey.if_true}')
#     print(f'    If false: throw to monkey {monkey.if_false}')


def run_round():
    global monkeys

    for i, monkey in enumerate(monkeys):
        print(f"Monkey {i}:")
        monkey.items = [item for item in monkey.items if item != -1]
        for i in range(len(monkey.items)):
            worry_level = monkey.items[i]
            print(f"  Monkey inspects an item with a worry level of {worry_level}.")

            new_worry_level = -1
            if monkey.op[1] == "old":
                if monkey.op[0] == "+":
                    new_worry_level = worry_level + worry_level
                    print(
                        f"    Worry level is increased by itself to {new_worry_level}."
                    )
                elif monkey.op[0] == "*":
                    new_worry_level = worry_level * worry_level
                    print(
                        f"    Worry level is multiplied by itself to {new_worry_level}."
                    )
            else:
                if monkey.op[0] == "+":
                    new_worry_level = worry_level + int(monkey.op[1])
                    print(
                        f"    Worry level increases by {int(monkey.op[1])} to {new_worry_level}."
                    )
                elif monkey.op[0] == "*":
                    new_worry_level = worry_level * int(monkey.op[1])
                    print(
                        f"    Worry level is multiplied by {int(monkey.op[1])} to {new_worry_level}."
                    )

            new_worry_level = new_worry_level // 3
            print(
                f"    Monkey gets bored with item. Worry level is divided by 3 to {new_worry_level}."
            )

            if new_worry_level % monkey.test == 0:
                print(f"    Current worry level is divisible by {monkey.test}.")
                monkeys[monkey.if_true].items.append(new_worry_level)
                print(f'    Item with worry level {new_worry_level} is thrown to monkey {monkey.if_true}.')
                monkey.items[i] = -1  # mark as thrown
            else:
                print(f"    Current worry level is not divisible by {monkey.test}.")
                monkeys[monkey.if_false].items.append(new_worry_level)
                print(f'    Item with worry level {new_worry_level} is thrown to monkey {monkey.if_false}.')
                monkey.items[i] = -1  # mark as thrown


# run simulation
for i in range(20):
    run_round()

    for monkey in monkeys:
        monkey.items = [item for item in monkey.items if item != -1]

    print(f'--END OF ROUND {i+1}---')
    for i, monkey in enumerate(monkeys):
        print(f'Monkey {i}: {monkey.items}')

