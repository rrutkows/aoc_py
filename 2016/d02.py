from util import data, runner

def solve(input):
    directions = dict(U = (0, -1), D = (0, 1), L = (-1, 0), R = (1, 0))
    code = []
    for l in input.splitlines():
        x, y = 1, 1
        for dx, dy in (directions[c] for c in l):
            x = max(0, min(2, x + dx))
            y = max(0, min(2, y + dy))
        code.append(f"{y * 3 + x + 1}")
    return ''.join(code)

if __name__ == "__main__":
    input = data.get_input(2016, 2)
    runner.run(lambda: solve(input))
