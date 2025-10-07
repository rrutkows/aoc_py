from collections import deque
from util import data, runner

D = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def solve(input, must_return):
    g = input.splitlines()
    largest = 0
    for y in range(len(g)):
        for x in range(len(g[y])):
            if g[y][x].isdigit():
                point = int(g[y][x])
                largest = max(point, largest)
                if point == 0:
                    start = (x, y)
    target = (1 << (largest + 1)) - 1 # bitmask of all points reached - all 1s
    q = deque([(start, 0, 1)]) # Q el is (coords, steps, points reached - bitfield)
    visited = set([(start, 1)]) # visited el is (coords, points reached - bitfield)
    while q:
        (x, y), steps, points = q.popleft()
        if (points == target and
                (not must_return or (x, y) == start)):
            return steps
        for dx, dy in D:
            new_x = x + dx
            new_y = y + dy
            if g[new_y][new_x] != '#':
                if g[new_y][new_x].isdigit():
                    point = int(g[new_y][new_x])
                    new_points = points | (1 << point)
                else:
                    new_points = points

                if ((new_x, new_y), new_points) not in visited:
                    visited.add(((new_x, new_y), new_points))
                    q.append(((new_x, new_y), steps + 1, new_points))

if __name__ == "__main__":
    input = data.get_input(2016, 24)
    runner.run(lambda: solve(input, False))
    runner.run(lambda: solve(input, True))