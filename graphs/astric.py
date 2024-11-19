import heapq

def a_star(graph, start, goal, heuristic):
    # Priority queue to store (cost, current_node, path)
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, current, path = heapq.heappop(pq)

        if current in visited:
            continue

        path = path + [current]
        visited.add(current)

        # If the goal is reached, return the path and cost
        if current == goal:
            return path, cost

        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                # f(n) = g(n) + h(n)
                new_cost = cost + weight
                estimated_cost = new_cost + heuristic(neighbor, goal)
                heapq.heappush(pq, (estimated_cost, neighbor, path))

    return None, float('inf')  # No path found

# Example Graph and Heuristic Function
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

def heuristic(node, goal):
    # Example heuristic: Straight-line distance (can be arbitrary values)
    heuristic_values = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
    return heuristic_values[node]

# Finding the shortest path from 'A' to 'D'
path, cost = a_star(graph, 'A', 'D', heuristic)
print(f"Shortest path: {path}, Cost: {cost}")
