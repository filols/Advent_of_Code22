from dijkstar import Graph, find_path

graph = Graph()
start = None
end = None

with open("input.txt", 'r') as file:
    value = lambda x: ord(x) if x.islower() else ord('z') if x == 'E' else ord('a')
    nodes = file.read().splitlines()
    every_a = set()

    # Edges x-led
    for y, row in enumerate(nodes):
        if start == None and 'S' in (index := row.index('S')):
            start = (index, y)
        if end == None and (index := 'E' in row):
            end = (index, y)

        for x, square in enumerate(row[:-1]):
            if (value(square) - value(row[x+1])) >= -1:
                graph.add_edge((x, y), (x+1, y), 1)
            if (value(row[x+1]) - value(square)) >= -1:
                graph.add_edge((x+1, y), (x, y), 1)
            if square == 'a':
                every_a.add((x, y))


    # Transpose
    nodes = list(zip(*nodes))

    # Edges y-led
    for x, column in enumerate(nodes):
        for y, square in enumerate(column[:-1]):
            if (value(square) - value(column[y+1])) >= -1:
                graph.add_edge((x, y), (x, y+1), 1)
            if (value(column[y+1]) - value(square)) >= -1:
                graph.add_edge((x, y+1), (x, y), 1)

    # Print steps
    print("Steps to highest elevation: %s" % list(find_path(graph, start, end))[-1])

    # Find closest 'a'
    distances = []
    for a in every_a:
        try:
            distance = list(find_path(graph, a, end))[-1]
            distances.append(distance)
        except:
            pass

    print("Hiking trail: %s" % min(distances))