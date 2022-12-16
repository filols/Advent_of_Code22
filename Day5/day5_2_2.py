def parse_crates(lines):
    stacks = []

    for i in range(1, len(lines[0]), 4):
        stack = [line[i] for line in lines[::-1] if line[i].isalpha()]
        stacks.append(stack)

    return stacks

def rearrangement(stacks, moves):
    for move in moves:
        amount, fromm, to = move
        from_size = len(stacks[fromm]) - amount
        
        for _ in range(amount):
            stacks[to].append(stacks[fromm].pop(from_size))


def main():
    with open("input.txt", 'r') as file:
        stacks, moves = file.read().split("\n\n")
        stacks = parse_crates(stacks.splitlines()[:-1])
        moves = moves.splitlines()
        moves = [(int(move[1]), int(move[3])-1, int(move[5])-1) for move in map(str.split(), moves)]
        rearrangement(stacks, moves)
        print("".join(s.pop() for s in stacks))
        
        
if __name__ == "__main__":
    main()