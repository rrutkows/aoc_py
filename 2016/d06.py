from collections import Counter
from util import data, runner

def _most_common(counter):
    return counter.most_common(1)[0][0]

def _least_common(counter):
    return counter.most_common()[-1][0]

def solve(input, get_character):
    it = iter(input.splitlines())
    l = next(it)
    counters = [Counter(c) for c in l]
    for l in it:
        for i, c in enumerate(l):
            counters[i].update(c)
    return ''.join(get_character(counter) for counter in counters)

def solve_alt(input, get_character):
    counters = (Counter(x) for x in zip(*input.splitlines()))
    return ''.join(get_character(counter) for counter in counters)

if __name__ == "__main__":
    input = data.get_input(2016, 6)
    runner.run(lambda: solve(input, _most_common))
    runner.run(lambda: solve(input, _least_common))
    runner.run(lambda: solve_alt(input, _most_common))
    runner.run(lambda: solve_alt(input, _least_common))
