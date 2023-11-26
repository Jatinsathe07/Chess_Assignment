from queue import Queue

def is_valid(x, y, n, m, grid):
    return 0 <= x < n and 0 <= y < m and grid[x][y] != 0

def find_meeting_point(n, m, horse_pos, bishop_pos, inactive_cells):
    grid = [[1] * m for _ in range(n)]

    for x, y in inactive_cells:
        grid[x][y] = 0

    horse_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    bishop_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    q = Queue()
    q.put((horse_pos[0], horse_pos[1], bishop_pos[0], bishop_pos[1], 0))

    while not q.empty():
        hx, hy, bx, by, steps = q.get()

        if hx == bx and hy == by:
            return (hx, hy)

        for move in horse_moves:
            nx, ny = hx + move[0], hy + move[1]
            if is_valid(nx, ny, n, m, grid):
                q.put((nx, ny, bx, by, steps + 1))

        for move in bishop_moves:
            nx, ny = bx + move[0], by + move[1]
            while is_valid(nx, ny, n, m, grid):
                q.put((hx, hy, nx, ny, steps + 1))
                nx, ny = nx + move[0], ny + move[1]

    return None

# Example usage:
n, m = 7, 7
horse_position = (6, 6)
bishop_position = (3, 2)
inactive_cells = [(0, 3), (2, 0)]

result = find_meeting_point(n, m, horse_position, bishop_position, inactive_cells)
print("Meeting point:", result)