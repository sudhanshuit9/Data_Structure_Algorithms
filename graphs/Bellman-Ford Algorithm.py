def bellman_ford(graph, start, vertices):
    distances = {vertex: float('inf') for vertex in vertices}
    distances[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative-weight cycles
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return distances

# Example
edges = [('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 4), ('C', 'D', 2)]
vertices = {'A', 'B', 'C', 'D'}
print(bellman_ford(edges, 'A', vertices))
