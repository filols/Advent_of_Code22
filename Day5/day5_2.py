def init_stacks(lines):
    for line in lines:
        if '[' not in line:
            return [[] for _ in range(int(line.split()[-1]))]


def add_crates(stacks, lines):
    for line in lines:
        if '[' not in line:
            [stack.reverse() for stack in stacks]
            return stacks

        column = 0
        for i in range(1, len(line), 4):
            crate_letter = line[i]
            if crate_letter.isalpha():
                stacks[column].append(crate_letter)
            column += 1


def parse_structure(lines):
    stacks = init_stacks(lines)
    stacks = add_crates(stacks, lines)
    return stacks


def parse_moves(lines, first_line):
    moves  = []
    
    for line_index in range (first_line, len(lines)):
        line = lines[line_index].split()
        moves.append((int(line[1]), int(line[3])-1, int(line[5])-1))
    
    return moves


def rearrangement(stacks, moves):
    for move in moves:
        amount, fromm, to = move
        from_size = len(stacks[fromm]) - amount
        
        for _ in range(amount):
            #if len(stacks[fromm]) <= from_size:
                #break
            
            stacks[to].append(stacks[fromm].pop(from_size))


def main():
    with open("input.txt", 'r') as file:
        lines = file.read().splitlines()
        stacks = parse_structure(lines)
        moves = parse_moves(lines, len(max(stacks, key=len))+2)
        rearrangement(stacks, moves)
        print("".join(s.pop() for s in stacks))
        
        
if __name__ == "__main__":
    main()