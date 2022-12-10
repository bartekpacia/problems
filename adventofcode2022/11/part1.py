class Monkey:
    def __init__(
        self,
        items: list[int]=[],
        op: tuple[str, str]=("None", "None"),
        test: int=-1,
        if_true: int=-1,
        if_false: int=-1,
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
            print('Appending monkey')   
            current_monkey = Monkey()
        elif line.startswith('Monkey'):
            pass
        elif line.startswith('Starting items'):
            current_monkey.items = list(map(lambda x: int(x), line.replace(',', '').split()[2:]))
        elif line.startswith('Operation'):
            op = line.split()[4]
            arg = line.split()[5]
            current_monkey.op = (op, arg)
        elif line.startswith('Test'):
            current_monkey.test = int(line.split()[3])
        elif line.startswith('If true'):
            current_monkey.if_true = int(line.split()[5])
        elif line.startswith('If false'):
            current_monkey.if_false = int(line.split()[5])
        
    monkeys.append(current_monkey)


for i, monkey in enumerate(monkeys):
    print(f'Monkey {i}')
    print(f'  Starting items: {monkey.items}')
    print(f'  Operation: new = old {monkey.op[0]} {monkey.op[1]}')
    print(f'  Test: divisible by {monkey.test}')
    print(f'    If true: throw to monkey {monkey.if_true}')
    print(f'    If false: throw to monkey {monkey.if_false}')
