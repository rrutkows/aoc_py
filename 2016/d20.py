
from util import data, runner

def solve(input):
    ranges = []
    for line in input.splitlines():
        l, h = list(map(int, line.split('-')))
        new = range(l, h + 1)
        r1, r2 = [], [new]
        for r in ranges:
            if l in r or h in r or l == r.stop or h == r.start - 1:
                r2.append(r)
            elif r.start not in new or r.stop not in new:
                r1.append(r)
        merged = range(
            min(r2, key=lambda r: r.start).start,
            max(r2, key=lambda r: r.stop).stop
        )
        r1.append(merged)
        ranges = r1

    ranges = sorted(ranges, key=lambda r: r.start)
    p1 = ranges[0].stop
    p2 = sum(r2.start - r1.stop for r1, r2 in zip(ranges, ranges[1:]))
    return p1, p2

if __name__ == "__main__":
    input = data.get_input(2016, 20)
    runner.run(lambda: solve(input))
