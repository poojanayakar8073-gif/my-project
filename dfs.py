# Define the tree using adjacency list
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

# DFS function (recursive)
def dfs(tree, node, visited):
    visited.append(node)

    for neighbor in tree[node]:
        dfs(tree, neighbor, visited)

    return visited


# MAIN
result = dfs(tree, 1, [])

print("DFS Traversal:")
print(" ".join(map(str, result)))