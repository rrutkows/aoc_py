from collections import deque
import re
from util import data, runner

D = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def solve01(input):
    pairs = 0
    nodes = []
    for line in input.splitlines()[2:]:
        n = list(map(int, re.findall(r'\d+', line)))
        used, avail = n[3], n[4]
        for n_used, n_avail in nodes:
            if n_used > 0 and avail >= n_used or used > 0 and n_avail >= used:
                pairs += 1
        nodes.append((used, avail))
    return pairs

def _parse(input):
    g = []
    for line in input.splitlines()[2:]:
        x, y, size, used, *_ = list(map(int, re.findall(r'\d+', line)))
        while y >= len(g):
            g.append([])
        assert x == len(g[y])
        g[y].append((size, used))
    return g

def _find_empty(g, W, H):
    for y in range(H):
        for x in range(W):
            size, used = g[y][x]
            for dx, dy in D:
                if (x + dx in range(W) and
                        y + dy in range(H) and
                        g[y + dy][x + dx][1] > 0 and
                        size - used >= g[y + dy][x + dx][1]):
                    return (x, y)

def solve02(input):
    start = _parse(input)
    W, H = len(start[0]), len(start)
    #print(W, H)
    only_used = [[node[1] for node in row] for row in start]
    empty = _find_empty(start, W, H)
    q = deque([(0, (W - 1, 0), empty, only_used)]) # Q el is (move count, data coords, empty coords, grid)
    visited = set([(W - 1, 0), empty]) # visited el is (data coords, empty coords)

    while q:
        move_count, (data_x, data_y), (x, y), g = q.popleft()
        if data_x == 0 and data_y == 0:
            return move_count

        size = start[y][x][0]
        for dx, dy in D:
            if (x + dx in range(W) and y + dy in range(H) and
                    size >= g[y + dy][x + dx]):
                moving_data = data_x == x + dx and data_y == y + dy
                new_data = (x, y) if moving_data else (data_x, data_y)
                new_empty = (x + dx, y + dy)
                if (new_data, new_empty) not in visited:
                    visited.add((new_data, new_empty))
                    new_g = [row[:] for row in g]
                    new_g[y][x] = g[y + dy][x + dx]
                    new_g[y + dy][x + dx] = 0
                    q.append((
                        move_count + 1,
                        new_data,
                        new_empty,
                        new_g
                    ))

if __name__ == "__main__":
    input = data.get_input(2016, 22)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))