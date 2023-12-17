from functools import cache
from itertools import repeat
from util import data, runner

def _solutions(row, pattern):
    @cache
    def recur(pos, group_id, group_amount):
        if pos == len(row):
            return 1 if group_id == len(pattern) or group_id == len(pattern) - 1 and group_amount == pattern[group_id] else 0
        else:
            result = 0
            if row[pos] != '#':
                if group_amount == 0:
                    result += recur(pos + 1, group_id, group_amount)
                elif group_amount == pattern[group_id]:
                    result += recur(pos + 1, group_id + 1, 0)
            if row[pos] != '.':
                if group_id < len(pattern) and group_amount < pattern[group_id]:
                    result += recur(pos + 1, group_id, group_amount + 1)
        return result
    return recur(0, 0, 0)

def solve(input, unfold):
    it = (l.split(' ') for l in input.splitlines())
    it = ((pair[0], list(map(int, pair[1].split(',')))) for pair in it)
    if unfold:
        it = (('?'.join(repeat(pair[0], 5)), pair[1] * 5) for pair in it)
    return sum(_solutions(*pair) for pair in it)

if __name__ == "__main__":
    input = data.get_input(2023, 12)
    runner.run(lambda: solve(input, False))
    runner.run(lambda: solve(input, True))
