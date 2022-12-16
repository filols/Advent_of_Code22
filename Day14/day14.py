from re import findall
from itertools import pairwise

def main():
    lowest = 0
    paths_set = set()
    with open("input.txt", 'r') as file:
        for line in file:
            for old, new in pairwise(findall(r'\d+\,\d+', line)):
                x, y = map(int, old.split(','))
                dx, dy = map(int, new.split(','))

                paths_set |= set([(x, y) for x in range(min(x, dx), max(x, dx)+1)])
                paths_set |= set([(x, y) for y in range(min(y, dy), max(y, dy)+1)])

                if (new_lowest := max(y, dy)) > lowest:
                    lowest = new_lowest
    
    # Falling sand
    sand_at_rest = 0
    x, y = 500, 0
    while True:
        if y >= lowest:
            break

        if (x, y+1) not in paths_set:
            y += 1
        elif (x-1, y+1) not in paths_set:
            x -= 1
            y += 1
        elif (x+1, y+1) not in paths_set:
            x += 1
            y += 1
        else:
            paths_set.add((x, y))
            sand_at_rest += 1
            x, y = 500, 0

    print("Abyss:", sand_at_rest)
 
    # Sand keeps falling with extended floor
    lowest += 2
    x, y = 500, 0
    while True:
        if (x, new_y := y+1) not in paths_set and new_y < lowest:
            y += 1
        elif (x-1, new_y := y+1) not in paths_set and new_y < lowest:
            x -= 1
            y += 1
        elif (x+1, new_y := y+1) not in paths_set and new_y < lowest:
            x += 1
            y += 1
        elif (x, y) == (500, 0):
            sand_at_rest += 1
            break
        else:
            paths_set.add((x, y))
            sand_at_rest += 1
            x, y = 500, 0

    print("With extended floor:", sand_at_rest)


if __name__ == "__main__":
    main()