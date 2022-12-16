def value(char):
    if char.islower():
        return ord(char)-96
    else:
        return ord(char)-38

with open("input.txt", 'r') as file:
    priority_sum = 0
    lines = file.read().splitlines()
    
    for i in range(0, len(lines), 3):
        line0 = set(lines[0])
        line1 = set(lines[i+1])
        for char in lines[i+2]:
            if char in line0 & char in line1:
                priority_sum += value(char) 
                continue

    print(priority_sum)