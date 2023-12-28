from collections import defaultdict
from util import data, runner
import re

_directions = dict(E = (-1, 0), N = (0, -1), W = (1, 0), S = (0, 1))

_terrain = {'.': 'ENWS', '<': 'E', '^': 'N', '>': 'W', 'v': 'S'}

def _nghbrs(x, y, grid):
    for dx, dy in (_directions[x] for x in _terrain[grid[y][x]]):
        yield x + dx, y + dy

def _parse(input, slope_as_path):
    grid = input.splitlines()
    if slope_as_path:
        grid = [re.sub(r'[<^>v]', '.', l) for l in grid]
    start = (grid[0].index('.'), 0)
    return grid, start

def solve01(input):
    grid, start = _parse(input, False)
    w, h = len(grid[0]), len(grid)
    result = 0
    q = [(start, {start})] #(coords, path)
    while q:
        c, path = q.pop()
        x, y = c
        while y != len(grid) - 1:
            def is_valid(x, y):
                return x in range(w) and y in range(h) \
                    and grid[y][x] != '#' \
                    and not (x, y) in path
            nghbrs = [c for c in _nghbrs(x, y, grid) if is_valid(*c)]
            if nghbrs:
                q.extend((next_c, path | {next_c}) for next_c in nghbrs[1:])
                x, y = nghbrs[0]
                path.add((x, y))
            else:
                break
        else:
            result = max(result, len(path) - 1)
    return result

def _to_graph(grid, start):
    w, h = len(grid[0]), len(grid)
    q = [(start, None, start, 0)] #(start (last crossroads), prev, current, length from start)
    g = defaultdict(list)
    seen = set()
    while q:
        start, prev, c, l = q.pop()
        if c in seen:
            continue
        seen.add(c)
        x, y = c
        def is_valid(x, y):
            return x in range(w) and y in range(h) \
                and grid[y][x] != '#' \
                and (x, y) != prev
        nghbrs = [n for n in _nghbrs(x, y, grid) if is_valid(*n)]
        if nghbrs:
            if len(nghbrs) > 1:
                for n in nghbrs:
                    if not n in seen:
                        q.append((c, c, n, 1))
                g[start].append((c, l))
                g[c].append((start, l))
            else:
                n = nghbrs[0]
                if n in seen:
                    g[start].append((n, l + 1))
                    g[n].append((start, l + 1))
                else:
                    q.append((start, c, n, l + 1))
        elif y == h - 1:
            g[start].append((c, l))
            g[c].append((start, l))
            end = c
    return g, end

def solve02(input):
    grid, start = _parse(input, True)
    g, end = _to_graph(grid, start)
    q = [(start, {start}, 0)]
    result = 0
    while q:
        node, path, distance = q.pop()
        if node == end:
            result = max(result, distance)
        else:
            for next, l in g[node]:
                if not next in path:
                    q.append((next, path | {next}, distance + l))
    return result

if __name__ == "__main__":
    input = data.get_input(2023, 23)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
