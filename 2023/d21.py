import math
from util import data, runner

_directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def _nghbrs(x, y):
    for dx, dy in _directions:
        yield x + dx, y + dy

def _parse(input):
    garden = []
    for y, l in enumerate(input.splitlines()):
        if 'S' in l:
            start = (l.index('S'), y)
            l = l.replace('S', '.')
        garden.append(l)
    return garden, start

def _solve(garden, start, steps, *, infinite = False):
    garden, start = _parse(input)
    w, h = len(garden[0]), len(garden)
    reached = {start}
    for _ in range(steps):
        next = set()
        for c in reached:
            for next_c in _nghbrs(*c):
                x, y = next_c
                in_range = infinite or (x in range(w) and y in range(h))
                if in_range and garden[y % h][x % w] == '.':
                    next.add(next_c)
        reached = next
    return len(reached)

def solve01(input):
    garden, start = _parse(input)
    return _solve(garden, start, 64)

def solve02(input):
    garden, start = _parse(input)
    # x0 = 0, x1 = 1, x2 = 2
    y0 = _solve(garden, start, 65)
    y1 = _solve(garden, start, 65 + 131, infinite = True)
    y2 = _solve(garden, start, 65 + 131 + 131, infinite = True)
    y = [y0, y1, y2]
    x = (26501365 - 65) // 131

    # Lagrange polynomial
    def l(j):
        return math.prod((x - m) / (j - m) for m in range(3) if m != j)
    return sum(y[j] * l(j) for j in range(3))

def solve02_vis(input):
    garden, start = _parse(input)
    w, h = len(garden[0]), len(garden)
    #print(w, h, start)
    #print(sum(c == '.' for l in garden for c in l)) 
    reached = {start}
    for _ in range(65 + 131):
        next = set()
        for c in reached:
            for next_c in _nghbrs(*c):
                x, y = next_c
                if garden[y % h][x % w] == '.':
                    next.add(next_c)
        reached = next
    print(len(reached))
    min_x = min(c[0] for c in reached)
    max_x = max(c[0] for c in reached)
    min_y = min(c[1] for c in reached)
    max_y = max(c[1] for c in reached)
    #print (min_x, min_y, max_x, max_y)
    def _c(x, y):
        if (x, y) in reached:
            return 'O'
        return garden[y % h][x % w] 
    for y in range(min_y, max_y + 1):
        print(''.join(_c(x, y) for x in range(min_x, max_x + 1)))


if __name__ == "__main__":
    input = data.get_input(2023, 21)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
