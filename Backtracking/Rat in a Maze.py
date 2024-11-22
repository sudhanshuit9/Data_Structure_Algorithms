#Find a path through a maze from the start to the destination
def rat_in_maze(maze):
    def is_safe(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1

    def solve(x, y):
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            solution[x][y] = 1
            return True
        if is_safe(x, y):
            solution[x][y] = 1
            if solve(x + 1, y) or solve(x, y + 1):
                return True
            solution[x][y] = 0
        return False

    solution = [[0] * len(maze[0]) for _ in range(len(maze))]
    if solve(0, 0):
        return solution
    return None

# Example
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
path = rat_in_maze(maze)
for row in path:
    print(row)
