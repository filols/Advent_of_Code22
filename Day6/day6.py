def distinct(buffer, consecutive_unique):
    marker = list(buffer[:consecutive_unique-1])
    buffer = list(buffer[consecutive_unique-1:])

    for i in range(consecutive_unique, len(buffer), 1):
        marker.append(buffer.pop(0))

        if len(set(marker)) == consecutive_unique:
            return i
        
        marker.pop(0)


def main():
    with open("input.txt", 'r') as file:
        buffer = file.read()
        print(distinct(buffer, 4))
        print(distinct(buffer, 14))


if __name__ == "__main__":
    main()