import re
from util import data, runner


def solve(input, extra):
    discs = (re.findall(r'(\d+)', x) for x in input.splitlines())
    discs = [(int(x[1]), int(x[3])) for x in discs] # [(positions, start), ...]
    if (extra != None):
        discs.append(extra)
    discs = [(x[0], (x[0] - x[1] - i - 1) % x[0]) for i, x in enumerate(discs)] # [(positions, remainder), ...]
    largest = max(enumerate(discs), key=lambda x: x[1][0]) # (index, (positions, remainder))
    ans = largest[1][1]
    while any(ans % x[0] != x[1] for i, x in enumerate(discs) if i != largest[0]):
        ans += largest[1][0]
    return ans

if __name__ == "__main__":
    input = data.get_input(2016, 15)
    runner.run(lambda: solve(input, None))
    runner.run(lambda: solve(input, (11, 0)))