from collections import deque 

def distinct(file, consecutive_unique):
    marker = deque(list(file.read(consecutive_unique-1)),consecutive_unique)
    processed = consecutive_unique-1
    char = file.read(1)

    while char:
        marker.append(char)
        processed += 1

        if len(set(marker)) == consecutive_unique:
            file.seek(0)
            return processed
        
        char = file.read(1)
        

def main():
    with open("input.txt", 'r') as file:
        print(distinct(file, 4))
        print(distinct(file, 14))


if __name__ == "__main__":
    main()