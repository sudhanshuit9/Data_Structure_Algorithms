def floyd_warshall(graph, vertices):
    dist = {v: {u: float('inf') for u in vertices} for v in vertices}
    for v in vertices:
        dist[v][v] = 0

    for u, v, weight in graph:
        dist[u][v] = weight

    for k in vertices:
        for i in vertices:
            for j in vertices:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example
edges = [('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 4), ('C', 'D', 2)]
vertices = {'A', 'B', 'C', 'D'}
print(floyd_warshall(edges, vertices))
