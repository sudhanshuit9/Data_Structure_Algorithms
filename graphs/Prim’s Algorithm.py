import heapq

def prim(graph, start):
    mst = []  # List to store edges in the Minimum Spanning Tree
    visited = set()  # Set of visited nodes
    min_heap = [(0, start, None)]  # Priority queue (weight, node, parent)

    while min_heap:
        weight, current_node, parent = heapq.heappop(min_heap)

        if current_node in visited:
            continue

        visited.add(current_node)
        if parent is not None:
            mst.append((parent, current_node, weight))

        for neighbor, edge_weight in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_node))

    return mst

# Example Graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
}

# Running Prim's Algorithm
mst = prim(graph, 'A')
print("Minimum Spanning Tree:", mst)
from collections import deque

def bfs(residual_graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        current_node = queue.popleft()

        for neighbor, capacity in residual_graph[current_node].items():
            if neighbor not in visited and capacity > 0:  # Check for unvisited nodes with capacity > 0
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current_node

                if neighbor == sink:  # Stop BFS if sink is reached
                    return True

    return False

def ford_fulkerson(graph, source, sink):
    # Initialize residual graph
    residual_graph = {u: dict(v) for u, v in graph.items()}
    parent = {}
    max_flow = 0

    # Augment the flow while there's a path from source to sink
    while bfs(residual_graph, source, sink, parent):
        # Find the maximum flow through the path found by BFS
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        # Update residual capacities of the edges and reverse edges
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow

# Example Graph
graph = {
    'A': {'B': 10, 'C': 10},
    'B': {'C': 2, 'D': 4, 'E': 8},
    'C': {'E': 9},
    'D': {'F': 10},
    'E': {'D': 6, 'F': 10},
    'F': {}
}

# Running Ford-Fulkerson Algorithm
source = 'A'
sink = 'F'
max_flow = ford_fulkerson(graph, source, sink)
print(f"Maximum Flow: {max_flow}")
