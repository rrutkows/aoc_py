import itertools
from util import data, runner

def solve(input, extra):
    it = iter(input.splitlines())
    first = next(it)
    empty_rows = set()
    empty_cols = set(range(0, len(first)))
    galaxies = list()
    for y, l in enumerate(itertools.chain([first], it)):
        if not "#" in l:
            empty_rows.add(y)
            continue
        for x, c in enumerate(l):
            if c == '#':
                empty_cols.discard(x)
                galaxies.append((x, y))
    
    def distance(g1, g2):
        return abs(g1[0] - g2[0]) + \
            abs(g1[1] - g2[1]) + \
            sum(extra for i in empty_cols if i in range(min(g1[0], g2[0]) + 1, max(g1[0], g2[0]))) + \
            sum(extra for i in empty_rows if i in range(min(g1[1], g2[1]) + 1, max(g1[1], g2[1])))
    
    return sum(distance(g1, g2) for g1, g2 in itertools.combinations(galaxies, 2))


if __name__ == "__main__":
    input = data.get_input(2023, 11)
    runner.run(lambda: solve(input, 1))
    runner.run(lambda: solve(input, 1000000 - 1))
