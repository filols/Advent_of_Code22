def main():
    with open("input.txt", 'r') as file:
        rows = [[int(height) for height in line] for line in list(map(list, file.read().splitlines()))]
        columns = list(zip(*rows))

        visible_interior_trees = 0
        for row_index in range(1, len(rows)-1):    
            for column_index in range(1, len(columns)-1):
                height = rows[row_index][column_index]

                # Horizontally visible
                if max(rows[row_index][:column_index]) < height or max(rows[row_index][column_index+1:]) < height:
                    visible_interior_trees += 1
                    continue
                
                # Vertically visible
                if max(columns[column_index][:row_index]) < height or max(columns[column_index][row_index+1:]) < height:
                    visible_interior_trees += 1
                    continue  

        exterior_trees = len(rows)*2 + (len(columns)-2)*2        
        print(visible_interior_trees + exterior_trees)  

if __name__ == "__main__":
    main()