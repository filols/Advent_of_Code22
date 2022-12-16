def main():
    with open("input.txt", 'r') as lines:
        pos_tail = (0, 0)
        pos_head = (0, 0)
        tail_positions_crossed = set()
        tail_positions_crossed.add(pos_tail)

        for line in lines:
            dir, steps = line.strip().split()

            for _ in range(int(steps)):
                old_head_y, old_head_x = pos_head
                match dir:
                    case "U": pos_head = (old_head_y - 1, old_head_x)
                    case "D": pos_head = (old_head_y + 1, old_head_x)
                    case "L": pos_head = (old_head_y, old_head_x - 1)
                    case "R": pos_head = (old_head_y, old_head_x + 1)

                offset = tuple(map(lambda x, y: abs(x - y), pos_head, pos_tail))
                if max(offset) > 1:
                    pos_tail = (old_head_y, old_head_x)
                    tail_positions_crossed.add(pos_tail)

        print(len(tail_positions_crossed))

if __name__ == "__main__":
    #start_time = time.time()
    main()
    #print("--- %s seconds ---" % (time.time() - start_time))