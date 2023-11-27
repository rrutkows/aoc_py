from util import data, runner

def get_coords(input, stop_when_twice):
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]
    directionIdx = 0
    turns = dict(L = -1, R = 1)
    instructions = ((x[:1], int(x[1:])) for x in input.split(", "))
    c = (0, 0)
    visited = set([c])
    for turn, steps in instructions:
        directionIdx = (directionIdx + turns[turn]) % len(directions)
        dx, dy = directions[directionIdx]
        if stop_when_twice:
            for _ in range(steps):
                c = (c[0] + dx, c[1] + dy)
                if c in visited:
                    return c
                visited.add(c)
        else:
            c = (c[0] + steps * dx, c[1] + steps * dy)
    return c

def solve(input, stop_when_twice):
    c = get_coords(input, stop_when_twice)
    return sum(map(abs, c))


if __name__ == "__main__":
    input = data.get_input()
    runner.run(lambda: solve(input, False))
    runner.run(lambda: solve(input, True))
