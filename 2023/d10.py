from util import data, runner

_dirs = "WNES"

_nghbrs = [
    ((-1, 0), "-LFS"), # W
    ((0, -1), "|7FS"), # N
    ((1, 0), "-J7S"), # E
    ((0, 1), "|LJS"), # S
]

_exits = {
    "|": "NS",
    "-": "EW",
    "L": "NE",
    "J": "NW",
    "7": "SW",
    "F": "SE",
    "S": "WNES"
}

def _get_exits(c, tiles):
    w, h = len(tiles[0]), len(tiles)
    maybe_dirs = _exits[tiles[c[1]][c[0]]]
    for d, pipes in (_nghbrs[i] for i in map(_dirs.index, maybe_dirs)):
        x, y = tuple(map(sum, zip(c, d)))
        if x in range(0, w) and y in range(0, h) and tiles[y][x] in pipes:
            yield (x, y)


def solve(input):
    tiles = list(input.splitlines())
    for y, l in enumerate(tiles):
        if 'S' in l:
            start = (l.index('S'), y)
            break
    # queue of (coords, previous coords, length, loop area)
    q = [(c, start, 1, (c[0] - start[0]) * start[1]) for c in _get_exits(start, tiles)]
    while q:
        c, prev, l, area = q.pop()
        if tiles[c[1]][c[0]] == 'S':
            return (l // 2, abs(area) - (l // 2) + 1)
        q.extend((
            next,
            c,
            l + 1,
            area + (next[0] - c[0]) * c[1])
                for next in _get_exits(c, tiles) if next != prev)

if __name__ == "__main__":
    input = data.get_input(2023, 10)
    runner.run(lambda: solve(input))
