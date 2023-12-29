from itertools import combinations, islice
from util import data, runner
import z3

def _parse(input):
    for l in input.splitlines():
        numbers = [int(x) for x in l.replace(' @ ', ', ').split(', ')]
        yield numbers[:3], numbers[3:]

def _line_coefficients(s):
    # y = ax + b
    x0, y0 = s[0][:2]
    dx, dy = s[1][:2]
    a = dy / dx
    b = y0 - a*x0
    return a, b

def _in_future(x, s):
    x0 = s[0][0]
    dx = s[1][0]
    return (x - x0) * dx > 0

def _xy_intersect(s1, s2, min, max):
    a1, b1 = _line_coefficients(s1)
    a2, b2 = _line_coefficients(s2)
    if a1 == a2:
        return False
    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return x >= min and x <= max \
        and y >= min and y <= max \
        and _in_future(x, s1) \
        and _in_future(x, s2)

def solve01(input, min, max):
    pairs = combinations(_parse(input), 2)
    return sum(_xy_intersect(*pair, min, max) for pair in pairs)

def solve02(input):
    x, y, z, dx, dy, dz = z3.Ints('x y z dx dy dz')
    s = z3.Solver()
    for h in islice(_parse(input), 3):
        s.add((dx - h[1][0]) * (h[0][1] - y) == (dy - h[1][1]) * (h[0][0] - x))
        s.add((dx - h[1][0]) * (h[0][2] - z) == (dz - h[1][2]) * (h[0][0] - x))
    s.check()
    m = s.model()
    return m[x].as_long() + m[y].as_long() + m[z].as_long()

if __name__ == "__main__":
    input, min, max = data.get_input(2023, 24), 200000000000000, 400000000000000
    runner.run(lambda: solve01(input, min, max))
    runner.run(lambda: solve02(input))
