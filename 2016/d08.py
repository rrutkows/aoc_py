from util import data, runner
import re

W = 50
H = 6

def _run_commands(input):
    d = [[0 for _ in range(W)] for _ in range(H)]
    for l in input.splitlines():
        if m := re.match(r'rect (\d+)x(\d+)', l):
            x, y = map(int, m.groups())
            for i in range(y):
                d[i][:x] = (1 for _ in range(x))
        elif m := re.match(r'rotate row y=(\d+) by (\d+)', l):
            y, r = map(int, m.groups())
            d[y] = [d[y][(i - r) % W] for i in range(W)]
        elif m := re.match(r'rotate column x=(\d+) by (\d+)', l):
            x, r = map(int, m.groups())
            col = [d[(i - r) % H][x] for i in range(H)]
            for y in range(H):
                d[y][x] = col[y]
        else:
            print(l)
    return d

def solve01(input):
    return sum(sum(row) for row in _run_commands(input))

def solve02(input):
    d = _run_commands(input)
    pixels = ' #'
    for row in d:
        print(''.join(pixels[x] for x in row))

if __name__ == "__main__":
    input = data.get_input(2016, 8)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
