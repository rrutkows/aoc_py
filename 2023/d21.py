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

def solve01(input):
    garden, start = _parse(input)
    w, h = len(garden[0]), len(garden)
    q = {start}
    for _ in range(64):
        next = set()
        for c in q:
            for next_c in _nghbrs(*c):
                x, y = next_c
                if x in range(w) and y in range(h) and garden[y][x] == '.':
                    next.add(next_c)
        q = next
    return len(q)

if __name__ == "__main__":
    input = data.get_input(2023, 21)
    runner.run(lambda: solve01(input))
