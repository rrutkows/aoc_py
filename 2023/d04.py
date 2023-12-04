from util import data, runner
from collections import defaultdict

def _get_matching_count(l):
    s1, s2 = l.split(': ')
    s1, s2 = s2.split(' | ')
    winning = set(s1.split())
    return sum(n in winning for n in s2.split())

def solve01(input):
    it = (_get_matching_count(l) for l in input.splitlines())
    return sum(pow(2, count - 1) if count > 0 else 0 for count in it)

def solve02(input):
    n = defaultdict(lambda: 1)
    result = 0
    for i, l in enumerate(input.splitlines()):
        result += n[i]
        for j in range(_get_matching_count(l)):
            n[i + j + 1] += n[i]
    return result


if __name__ == "__main__":
    input = data.get_input(2023, 4)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
