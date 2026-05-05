# Tree representation (adjacency list)
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

# Depth-Limited Search (DLS)
def dls(tree, node, depth_limit, visited):
    visited.append(node)

    if depth_limit == 0:
        return

    for neighbor in tree[node]:
        dls(tree, neighbor, depth_limit - 1, visited)


# Iterative Deepening DFS (IDDFS)
def iddfs(tree, start, max_depth):
    for depth in range(max_depth + 1):
        visited = []
        dls(tree, start, depth, visited)
        print(f"Depth Limit {depth}: Visited nodes {visited}")


# MAIN

print("Depth-Limited Search (limit = 2):")
visited_nodes = []
dls(tree, 1, 2, visited_nodes)
print("Visited nodes:", visited_nodes)

print("\nIterative Deepening DFS:")
iddfs(tree, 1, 2)