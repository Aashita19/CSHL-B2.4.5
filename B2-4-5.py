
def find_shortest_path(grid, row, col, visited, steps):

    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return float('inf')

    if grid[row][col] == '#' or grid[row][col] == 'X' or visited[row][col]:
        return float('inf')

    if grid[row][col] == 'E':
        return steps

    visited[row][col] = True

    up = find_shortest_path(grid, row - 1, col, visited, steps + 1)
    down = find_shortest_path(grid, row + 1, col, visited, steps + 1)
    left = find_shortest_path(grid, row, col - 1, visited, steps + 1)
    right = find_shortest_path(grid, row, col + 1, visited, steps + 1)

    shortest = min(up, down, left, right)

    visited[row][col] = False

    return shortest

def solve(grid):
    start_row = -1
    start_col = -1

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                start_row = r
                start_col = c

    visited = [
        [False for _ in range(len(grid[0]))]
        for _ in range(len(grid))
    ]

    result = find_shortest_path(
        grid, start_row, start_col, visited, 0
    )

    if result == float('inf'):
        return -1

    return result

# test
map1 = [
    ['S', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '#', 'X', '#', '.'],
    ['.', '.', '.', '.', 'E']
]

map2 = [
    ['S', '#', '.', '.'],
    ['#', '#', '.', '.'],
    ['.', '.', 'X', '.'],
    ['.', '.', '.', 'E']
]

map3 = [
    ['S', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', 'E'],
    ['.', '.', '.', '.', '.']
]

map4 = [['S', 'E']]

print("Map 1:", solve(map1))
print("Map 2:", solve(map2))
print("Map 3:", solve(map3))
print("Map 4:", solve(map4))
