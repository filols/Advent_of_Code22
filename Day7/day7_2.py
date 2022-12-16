TOTAL_DISK_SPACE = 70000000
UPDATE_SIZE      = 30000000

def all_directories(file, all_dirs):
    current_folder_size = 0

    for line in file:
        if "$ cd .." in line:
            break

        elif "$ cd" in line:
            nested_folder_size = all_directories(file, all_dirs)
            current_folder_size += nested_folder_size

        elif line.split()[0].isnumeric():
            current_folder_size += int(line.split()[0])

    all_dirs.append(current_folder_size)
    return current_folder_size


def freed_space(all_dirs):
    space_taken = max(all_dirs)
    space_needed = space_taken - (TOTAL_DISK_SPACE - UPDATE_SIZE)
    return min([viable_dir for viable_dir in all_dirs if viable_dir >= space_needed])


def min_directory(file):
    all_dirs = []
    all_directories(file, all_dirs)
    return freed_space(all_dirs)


def main():
    with open("input.txt", 'r') as file:
        print(min_directory(file))


if __name__ == "__main__":
    main()