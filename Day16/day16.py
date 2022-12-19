import re
from collections import deque
from itertools import chain, combinations, product
from time import time

class Edge():
    def __init__(self, root, to, cost, rate):
        self.root = root
        self.to = to
        self.cost = cost
        self.to_rate = rate

    def __str__(self):
        return f"({self.root}:{self.to}, C:{self.cost}, R:{self.to_rate}.)"

    def __repr__(self):
        return self.__str__()

    # Cost to move and to open valve (cost + 1)
    def cost_to_open(self):
        return self.cost + 1

    # Pressure generated for remaining duration
    def points(self, moves_left):
        return (moves_left - self.cost - 1) * self.to_rate

# Traverses original graph. Adds direct edges between nodes with rate > 0 and between 
# aforementioned nodes and start node. 
def efficient_graph(graph: dict, nodes_with_rate: dict, root=['AA']):
    efficient_graph = {}
    nodes_with_rate_keys = set(nodes_with_rate.keys())
    node_to_tuple = lambda n, c: (n, c) 

    for node in chain(root, nodes_with_rate_keys):
        visited = set(); visited.add(node)
        edges = graph[node]
        
        # Combine node with cost in BFS search below. n = node, c = cost. 
        deq = deque(map(node_to_tuple, edges, [1 for _ in range(len(edges))]))

        # Init edge list for key if key not yet in graph.
        if not node in efficient_graph.keys():
            efficient_graph[node] = []

        # Stop when all nodes with rate > 0 have been visited.
        while not nodes_with_rate_keys.issubset(visited):
            next, curr_cost = deq.popleft()
            
            if next in visited:
                continue
            
            visited.add(next)
            next_nexts = map(node_to_tuple, graph[next], 
                            [curr_cost + 1 for _ in range(len(graph[next]))])
            deq.extend(next_nexts)
            
            if next in nodes_with_rate_keys:
                rate = nodes_with_rate[next]
                edges = efficient_graph[node]
                edges.append(Edge(node, next, curr_cost, rate))
    
    return efficient_graph

# Solves best points
# Start valve: AA; Moves: 30
# Points for releasing pressure = rate * ticks while rate is active 
#                               = (moves_left - cost_to_move - 1 [for opening valve]) * rate
def max_pressure(graph: dict, moves_left: int, root='AA') -> int:
    highest = 0
    current = 0
    for edge in graph[root]:
        if moves_left > (cost := edge.cost_to_open()) and edge.to in graph.keys(): 
            graph_without_visited = graph.copy()
            graph_without_visited.pop(root)
            current = edge.points(moves_left)
            current += max_pressure(graph_without_visited, moves_left - cost, edge.to)
        highest = current if current > highest else highest
    return highest


def main():
    graph = {}
    nodes_with_rate = {}
    
    # Parse and graph all edges
    with open('input.txt', 'r') as file:
        for line in file:
            valves = re.findall(r'[A-Z]{2}', line)
            node, to_nodes = valves[0], valves[1:]
            graph[node] = to_nodes

            if (rate := int(re.search(r'\d+', line).group())) > 0:
                nodes_with_rate[node] = rate

    # Reduce data set & evaluate pressure
    graph = efficient_graph(graph, nodes_with_rate)
    print("Most pressure:", max_pressure(graph, 30))
    

if __name__ == "__main__":
    t0 = time()
    main()
    print("Runtime:", time()-t0)