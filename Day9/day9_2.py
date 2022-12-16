def main():
    with open("input.txt", 'r') as lines:
        get_offset = lambda head, tail: tuple(map(lambda x, y: abs(x - y), head, tail))
        knots = [(0,0) for _ in range(10)]
        tail_positions_crossed = set()
        tail_positions_crossed.add((0, 0))

        for line in lines:
            dir, steps = line.strip().split()

            for _ in range(int(steps)):
                old_head_y, old_head_x = knots[0]
                match dir:
                    case "U": knots[0] = (old_head_y - 1, old_head_x)
                    case "D": knots[0] = (old_head_y + 1, old_head_x)
                    case "L": knots[0] = (old_head_y, old_head_x - 1)
                    case "R": knots[0] = (old_head_y, old_head_x + 1)
                
                for index in range(len(knots)-1):
                    head = knots[index]
                    tail = knots[index+1]
                    
                    offset = get_offset(head, tail)

                    if max(offset) > 1:
                        tail_movables = [(y, x) for y in range(tail[0]-1, tail[0]+2) for x in range(tail[1]-1, tail[1]+2) if not (y, x) == tail]
                        tail_movables = list(map(lambda square: (*square, sum(get_offset(head, square))), tail_movables))
                        tail = tuple(min(tail_movables, key = lambda t: t[2])[:2])
                        knots[index+1] = tail
                    else:
                        break
                
                tail_positions_crossed.add(knots[-1])
 
        print("Crossed:", len(tail_positions_crossed))

if __name__ == "__main__":
    #startt_time = time.time()
    main()
    #print("--- %s seconds ---" % (time.time() - startt_time))