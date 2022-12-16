with open("cals.txt", 'r') as file:
    list = []
    cals = 0

    for line in file:
        if line.startswith('\n'):
            list.append(cals)
            cals = 0
            continue
        cals = cals + int(line)
        
    print(sum(sorted(list)[-3:]))