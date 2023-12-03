from util import data, runner
import itertools, re

_is_symbol = lambda c: not c.isdigit() and c != '.'
_is_gear = lambda c: c == '*'

def solve01(input):
    adj = set()
    result = 0
    for y, l in enumerate(input.splitlines()):
        w = len(l)
        for x, c in enumerate(l):
            if _is_symbol(c):
                if x > 0:
                    adj.add((y - 1) * w + x - 1)
                    adj.add(y * w + x - 1)
                    adj.add((y + 1) * w + x - 1)
                if x < w - 1:
                    adj.add((y - 1) * w + x + 1)
                    adj.add(y * w + x + 1)
                    adj.add((y + 1) * w + x + 1)
                adj.add((y - 1) * w + x)
                adj.add((y + 1) * w + x)
    for y, l in enumerate(input.splitlines()):
        w = len(l)
        for m in re.finditer(r'\d+', l):
            if any(x in adj for x in range(y * w + m.start(), y * w + m.end())):
                result += int(m.group())
    return result

def solve02(input):
    result = 0
    lines = [''] + input.splitlines() + ['']
    for prev, cur, next in zip(lines, lines[1:], lines[2:]):
        for x, c in enumerate(cur):
            if _is_gear(c):
                prod, count = 1, 0
                for m in itertools.chain.from_iterable(re.finditer(r'\d+', l) for l in (prev, cur, next)):
                    if any(pos >= x - 1 and pos <= x + 1 for pos in (m.start(), m.end() - 1)):
                        prod, count = prod * int(m.group()), count + 1
                if count == 2:
                    result += prod
    return result


if __name__ == "__main__":
    input = data.get_input(2023, 3)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
