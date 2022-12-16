with open("input.txt", 'r') as file:
    overlap = 0
    
    for line in file:
        assignments = line.strip().split(',')
        range1_start, range1_end = assignments[0].split('-')
        range2_start, range2_end = assignments[1].split('-')
        if not (int(range1_start) > int(range2_end) or int(range2_start) > int(range1_end)):
            overlap += 1

    print(overlap)