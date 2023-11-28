from util import data, runner
import itertools

def _is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def solve01(input):
    parsed = (map(int, l.split()) for l in input.splitlines())
    return sum(1 for x in parsed if _is_triangle(*x))

def solve02(input):
    parsed = (tuple(map(int, l.split())) for l in input.splitlines())
    s = 0
    while b := list(itertools.islice(parsed, 3)):
        s += sum(1 for i in range(3) if _is_triangle(b[0][i], b[1][i], b[2][i]))
    return s

if __name__ == "__main__":
    input = data.get_input(2016, 3)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
