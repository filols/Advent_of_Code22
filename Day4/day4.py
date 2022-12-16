with open("input.txt", 'r') as file:
    fully_contained = 0
    
    for line in file:
        assignments = line.strip().split(',')
        range1_start, range1_end = assignments[0].split('-')
        range2_start, range2_end = assignments[1].split('-')
        if (int(range1_start) <= int(range2_start) and int(range1_end) >= int(range2_end) or
            int(range2_start) <= int(range1_start) and int(range2_end) >= int(range1_end)):
            fully_contained += 1

    print(fully_contained)