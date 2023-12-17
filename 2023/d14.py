from functools import reduce
from util import data, runner

def solve01(input):
    result = 0
    platform = input.splitlines()
    stops_at = [len(platform) for _ in platform[0]]
    for y, l in enumerate(platform):
        for x, c in enumerate(l):
            match c:
                case 'O':
                    result += stops_at[x]
                    stops_at[x] -= 1
                case '#':
                    stops_at[x] = len(platform) - y - 1
    return result

def _tilt_up(platform):
    next = list(list('.' for _ in row) for row in platform)
    stops_at = [0 for _ in platform[0]]
    for y, row in enumerate(platform):
        for x, c in enumerate(row):
            match c:
                case 'O':
                    next[stops_at[x]][x] = c
                    stops_at[x] += 1
                case '#':
                    next[y][x] = c
                    stops_at[x] = y + 1
    return next

def _rotate_clockwise(platform):
    return list(map(list, zip(*reversed(platform))))

def solve02(input):
    platform = list(list(l) for l in input.splitlines())
    record = []
    cycles = 1000000000
    for i in range(cycles):
        next = reduce(lambda acc, _: _rotate_clockwise(_tilt_up(acc)), range(4), platform)
        try:
            cycle_start = record.index(next)
            cycle_length = i - cycle_start
            remaining = cycles - cycle_start
            last = record[cycle_start + (remaining + cycle_length - 1) % cycle_length]
            break
        except ValueError:
            record.append(next)
            platform = next

    return sum((len(last) - y) * sum(c == 'O' for c in row) for y, row in enumerate(last))

if __name__ == "__main__":
    input = data.get_input(2023, 14)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
