import heapq

# ----------------------------
# (A) PUZZLE CLASS
# ----------------------------
class Puzzle:
    def __init__(self, state, parent=None, move="", cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost  # g(n)

    def display(self):
        for row in self.state:
            print(row)
        print()

    def is_goal(self, goal):
        return self.state == goal

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    # Generate successors (UP, DOWN, LEFT, RIGHT)
    def get_successors(self):
        x, y = self.find_blank()
        moves = [
            (-1, 0, "Move Up"),
            (1, 0, "Move Down"),
            (0, -1, "Move Left"),
            (0, 1, "Move Right")
        ]

        successors = []

        for dx, dy, move_name in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in self.state]

                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                successors.append(Puzzle(new_state, self, move_name, self.cost + 1))

        return successors


# ----------------------------
# HEURISTIC (Manhattan Distance)
# ----------------------------
def heuristic(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                value = state[i][j]

                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == value:
                            distance += abs(i - x) + abs(j - y)
    return distance
