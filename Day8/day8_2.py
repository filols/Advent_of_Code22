def visibility(trees, height):
    visibility = 0
    for tree in trees:
        visibility += 1
        if height <= tree:
            break

    return visibility

def main():
    with open("input.txt", 'r') as file:
        rows = [[int(height) for height in line] for line in list(map(list, file.read().splitlines()))]
        columns = list(zip(*rows))
        print(rows)
        print()
        print(columns)

        scenic_scores = []
        for row_index in range(1, len(rows)-1):    
            for column_index in range(1, len(columns)-1):
                height = rows[row_index][column_index]
                score = 1

                score *= (visibility(rows[row_index][:column_index][::-1], height))
                score *= (visibility(rows[row_index][column_index+1:], height))
                score *= (visibility(columns[column_index][:row_index][::-1], height))
                score *= (visibility(columns[column_index][row_index+1:], height))

                scenic_scores.append(score)

        print(max(scenic_scores))  

if __name__ == "__main__":
    main()

