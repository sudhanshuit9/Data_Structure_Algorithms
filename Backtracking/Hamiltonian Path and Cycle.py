#A Hamiltonian Path visits every vertex of a graph exactly once. If it forms a cycle, it is a Hamiltonian Cycle.
def hamiltonian_path(graph, path, visited, pos):
    if pos == len(graph):
        return graph[path[pos - 1]][path[0]] == 1

    for vertex in range(len(graph)):
        if graph[path[pos - 1]][vertex] == 1 and not visited[vertex]:
            path[pos] = vertex
            visited[vertex] = True
            if hamiltonian_path(graph, path, visited, pos + 1):
                return True
            visited[vertex] = False
    return False

def hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0
    visited = [False] * len(graph)
    visited[0] = True
    return hamiltonian_path(graph, path, visited, 1)

# Example
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
print("Hamiltonian Cycle exists:" if hamiltonian_cycle(graph) else "No Hamiltonian Cycle")
