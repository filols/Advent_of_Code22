from itertools import zip_longest
from functools import cmp_to_key

def in_order(left, right):
    # Couple every left[i] right[i] as (left[i], right[i]), default to None if either is missing
    pairs = list(zip_longest(left, right))

    for pair in pairs:
        left, right = pair

        # If (left == None) left input was exhausted without any elements out of order.
        # If (left != None) but (right == None) right input was exhausted first => out of order
        if left == None:
            return -1
        elif right == None:
            return 1

        # If either element of the pair is a list, recursively run with both elements as lists
        # If packet is solved, True/False is received and returned. If still undecided, None is 
        # received and the algorithm continues.
        elif isinstance(left, list) or isinstance(right, list):
            left = [left] if isinstance(left, int) else left
            right = [right] if isinstance(right, int) else right
            if not (was_in_order := in_order(left, right)):
                continue
            else:
                return was_in_order

        # If elements are equal, packet is undecided and algorithm continues
        elif left == right:
            continue
        
        # If reached, the pair consists of differing integers and (left < right) is returned
        else:
            return -1 if left < right else 1
    
    # Returns None if no conclusion about packet is reached
    return 0 

def main():
    with open("input.txt", 'r') as file:
        score = 0
        packets = []
        packets.append([[2]])
        packets.append([[6]])

        for count, pair in enumerate(file.read().split("\n\n"), 1):
            left, right = eval(pair.replace('\n', ','))
            packets.append(left)
            packets.append(right)
            if in_order(left, right) == -1:
                score += count 

        packets = sorted(packets, key=cmp_to_key(in_order))
        print(score)
        print((packets.index([[2]])+1)*(packets.index([[6]])+1))

if __name__ == "__main__":
    main()