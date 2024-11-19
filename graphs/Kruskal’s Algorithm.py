def kruskal(graph, vertices):
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        root1, root2 = find(v1), find(v2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    mst = []
    edges = sorted(graph, key=lambda edge: edge[2])  # Sort by weight

    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))

    return mst

# Example
edges = [('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 4), ('C', 'D', 2)]
vertices = {'A', 'B', 'C', 'D'}
print(kruskal(edges, vertices))
