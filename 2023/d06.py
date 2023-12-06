from util import data, runner
import math

def _solve(t, r):
    #-x^2 + tx - r > 0
    a, b, c = -1, t, -r
    d = b**2 - 4*a*c
    x1, x2 = (-b - math.sqrt(d))/(2 * a), (-b + math.sqrt(d)) / (2 * a)
    return abs(math.floor(x2) - math.floor(x1))

def solve01(input):
    it = iter(input.splitlines())
    times = map(int, next(it).split(':')[1].split())
    records = map(int, next(it).split(':')[1].split())
    return math.prod(_solve(*x) for x in zip(times, records))

def solve02(input):
    it = iter(input.splitlines())
    t = int(next(it).split(':')[1].replace(' ', ''))
    r = int(next(it).split(':')[1].replace(' ', ''))
    return _solve(t, r)

if __name__ == "__main__":
    input = data.get_input(2023, 6)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
