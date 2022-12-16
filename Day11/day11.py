import operator, re
from sys import maxsize as MAXSIZE

class Monkey:
    def __init__(self, items, op, op_args, divisible_by, true_monkey, false_monkey):
        self.items = items
        self.items_inspected = 0
        self.operator = op
        self.op_args = op_args
        self.divisible_by = divisible_by
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.mod = MAXSIZE

    def __str__(self):
        return (f"Items: {self.items}\nItems inspected: {self.items_inspected}")

    def __calc_worry(self, worry_level):
        args = self.op_args.copy()
        while len(args) < 2: args.append(worry_level)
        return self.operator(*args) % self.mod # // 3

    def __test(self, worry_level):
        return worry_level % self.divisible_by == 0

    def __throw_item(self, item):
        self.items_inspected += 1
        return (item, self.true_monkey) if self.__test(item) else (item, self.false_monkey)

    def throw_items(self):
        for item in self.items:
            item = self.__calc_worry(item)
            yield self.__throw_item(item)
        self.items.clear()

    def get_inspected_items(self):
        return self.items_inspected

    def receive_item(self, item):
        self.items.append(item)

    def set_mod(self, mod):
        self.mod = mod

    def get_divisible_by(self):
        return self.divisible_by


class Monkeys:
    def __init__(self):
        self.monkeys = []

    def __str__(self):
        monkeys = ''
        for count, monkey in enumerate(self.monkeys):
            monkeys += f"Monkey: {count}\n{monkey.__str__()}\n\n"
        return monkeys.rstrip()

    def __monkey_business(self):
        for monkey in self.monkeys:
            for item, to_monkey in monkey.throw_items():
                self.monkeys[to_monkey].receive_item(item)

    def round(self, rounds=1):
        for _ in range(rounds):
            self.__monkey_business()

    def parse_monkeys(self, file):
        ops = { '+': operator.add,
                '*': operator.mul
        }

        for line in file:
            if "Monkey" in line:
                items = list(map(int, re.findall(r'\d+', file.readline())))
                line = file.readline()
                op = ops[re.search(f'[{"".join(list(ops.keys()))}]', line).group()]
                op_args = list(map(int, re.findall(r'\d+', line)))
                divisible_by = int(re.search('\d+', file.readline()).group())
                true_monkey = int(re.search('\d+', file.readline()).group())
                false_monkey = int(re.search('\d+', file.readline()).group())
                self.monkeys.append(Monkey(items, op, op_args, divisible_by, true_monkey, false_monkey))
        self.__set_mod()

    def product_of_most_active_monkeys(self):
        inspected_items = sorted([monkey.get_inspected_items() for monkey in self.monkeys], reverse=True)
        return inspected_items[0] * inspected_items[1]

    def __set_mod(self):
        mod = 1
        for monkey in self.monkeys:
            mod *= monkey.get_divisible_by()
        for monkey in self.monkeys:
            monkey.set_mod(mod)


def main():
    monkeys = Monkeys()
    with open("input.txt", 'r') as file:
        monkeys.parse_monkeys(file)

    monkeys.round(10000)
    print(monkeys)
    print("Highest product:", monkeys.product_of_most_active_monkeys())


if __name__ == "__main__":
    main()