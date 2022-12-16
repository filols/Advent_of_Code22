MAX_TOTAL_SIZE = 100000

def allowed_directories(file, allowed_dirs):
    current_folder_size = 0

    for line in file:
        if "$ cd .." in line:
            break

        elif "$ cd" in line:
            nested_folder_size = allowed_directories(file, allowed_dirs)
            current_folder_size += nested_folder_size
            
        elif line.split()[0].isnumeric():
            current_folder_size += int(line.split()[0])
            
    if current_folder_size <= MAX_TOTAL_SIZE: 
        allowed_dirs.append(current_folder_size)
    return current_folder_size


def sum_directories(file):
    allowed_dirs = []
    allowed_directories(file, allowed_dirs)
    return sum(allowed_dirs)


def main():
    with open("input.txt", 'r') as file:
        print(sum_directories(file))


if __name__ == "__main__":
    main()  