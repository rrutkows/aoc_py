from itertools import chain
from util import data, runner

_directions = dict(W = (-1, 0), N = (0, -1), E = (1, 0), S = (0, 1))
_transitions = dict(
    W = {'.': 'W', '-': 'W', '|': 'NS', '/': 'S', '\\': 'N'},
    N = {'.': 'N', '-': 'WE', '|': 'N', '/': 'E', '\\': 'W'},
    E = {'.': 'E', '-': 'E', '|': 'NS', '/': 'N', '\\': 'S'},
    S = {'.': 'S', '-': 'WE', '|': 'S', '/': 'W', '\\': 'E'},
)

def _solve(cave, start_c, start_dir):
    w, h = len(cave[0]), len(cave)
    q = [(start_c, start_dir)]
    visited = set()
    energized = set()
    while q:
        c, dir = q.pop()
        energized.add(c)
        visited.add((c, dir))
        x, y = c
        for new_dir in _transitions[dir][cave[y][x]]:
            dx, dy = _directions[new_dir]
            next = ((x + dx, y + dy), new_dir)
            if not next in visited and next[0][0] in range(w) and next[0][1] in range(h):
                q.append(next)
    return len(energized)

def solve01(input):
    cave = input.splitlines()
    return _solve(cave, (0, 0), 'E')

def solve02(input):
    cave = input.splitlines()
    return max(_solve(cave, (x, y), d) for x, y, d in chain(
        ((x, 0, 'S') for x in range(len(cave[0]))),
        ((x, len(cave) - 1, 'N') for x in range(len(cave[0]))),
        ((0, y, 'E') for y in range(len(cave))),
        ((len(cave[0]) - 1, y, 'W') for y in range(len(cave)))
    ))

if __name__ == "__main__":
    input = data.get_input(2023, 16)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
