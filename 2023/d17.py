from collections import defaultdict
from heapq import heapify, heappop, heappush
from util import data, runner

_directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def _nghbrs(c, current_dir, steps_in_current_dir, min_steps, max_steps):
    x, y = c
    idx = []
    if steps_in_current_dir < max_steps:
        # go forward
        idx.append(current_dir)
    if steps_in_current_dir >= min_steps:
        # turn
        idx.extend((current_dir + i) % 4 for i in [1, 3])
    for i in idx:
        steps_in_dir = steps_in_current_dir if i == current_dir else 0
        dx, dy = _directions[i]
        yield (x + dx, y + dy), i, steps_in_dir + 1

def solve(input, min_steps, max_steps):
    grid = list(list(int(c) for c in l) for l in input.splitlines())
    w, h = len(grid[0]), len(grid)
    result = float("inf")
    # element: (coordinates, current direction, steps in current direction)
    # queue item: (heat loss from start, element)
    # initial directions: S, E (2, 3)
    q = [(0, ((0, 0), d, 0)) for d in [2, 3]]
    heapify(q)
    visited = defaultdict(lambda: float("inf"))
    while q:
        cost, el = heappop(q)
        for next in _nghbrs(*el, min_steps, max_steps):
            x, y = next[0]
            if x in range(w) and y in range(h):
                next_cost = cost + grid[y][x]
                if next_cost < visited[next] and next_cost < result:
                    visited[next] = next_cost
                    if x == w - 1 and y == h - 1 and next[2] >= min_steps:
                        result = next_cost
                    else:
                        heappush(q, (next_cost, next))
    return result

if __name__ == "__main__":
    input = data.get_input(2023, 17)
    runner.run(lambda: solve(input, 0, 3))
    runner.run(lambda: solve(input, 4, 10))
