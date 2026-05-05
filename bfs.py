from collections import deque

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

# BFS function
def bfs(tree, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        visited.append(node)

        for neighbor in tree[node]:
            queue.append(neighbor)

    return visited


# MAIN
result = bfs(tree, 1)

print("BFS Traversal:")
print(" ".join(map(str, result)))