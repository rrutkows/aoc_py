from itertools import takewhile
from util import data, runner

def _may_have_smudge(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1

def _find_reflection(x, find_smudge):
    for i in range(1, len(x)):
        found_smudge = False
        for j in range(min(i, len(x) - i)):
            if x[i - j - 1] != x[i + j]:
                if not find_smudge or found_smudge:
                    break
                elif _may_have_smudge(x[i - j - 1], x[i + j]):
                    found_smudge = True
                else:
                    break
        else:
            if not find_smudge or found_smudge:
                return i

def _parse(input):
    it = iter(input.splitlines())
    while rows := list(takewhile(lambda l: l, it)):
        cols = list(''.join(x) for x in zip(*rows))
        yield(rows, cols)

def solve(input, find_smudge):
    result = 0
    for rows, cols in _parse(input):
        if x := _find_reflection(cols, find_smudge):
            result += x
        else:
            result += 100 * _find_reflection(rows, find_smudge)
    return result

if __name__ == "__main__":
    input = data.get_input(2023, 13)
    runner.run(lambda: solve(input, False))
    runner.run(lambda: solve(input, True))
