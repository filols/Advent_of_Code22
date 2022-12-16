with open("input.txt", 'r') as file:
    priority_sum = 0

    for line in file:
        shared_element = set(line[:len(line)//2]).intersection(set(line[len(line)//2:])).pop()
        if shared_element.islower():
            priority_sum += ord(shared_element)-96
        else:
            priority_sum += ord(shared_element)-38
        
    print(priority_sum)