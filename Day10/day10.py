register = 1

def addx(x: str) -> None:
    yield
    yield
    global register
    register += int(x)

def update(cycle: int, ss: dict, pixels: list[list[str]]) -> int:
    ss[cycle] = register * cycle
    pixels[cycle-1] = '#' if (cycle-1)%40 in range(register-1, register+2) else '.'
    
def main():
    functions = {"addx": addx}
    cycle = 1
    ss = {}
    pixels = ['.' for _ in range(40*6)]

    with open("input.txt", 'r') as inputs:
        for input in inputs:
            try:
                instruction, arg = input.rstrip().split(' ')
                for _ in functions[instruction](arg):
                    update(cycle, ss, pixels)
                    cycle += 1
            except ValueError: #noop
                update(cycle, ss, pixels)
                cycle += 1

    sum = 0
    
    for i in range(0, len(pixels), 40):
        print(pixels[i:i+40])
    for i in range(20, 221, 40):
        sum += ss[i]
    print(sum)

if __name__ == "__main__":
    main()