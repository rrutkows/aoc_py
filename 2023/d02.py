from util import data, runner
import operator, math, re

R = 12
G = 13
B = 14
BAG = (R, G, B)

def _parse_hand(s):
    for c in ["red", "green", "blue"]:
        m = re.search(r'(\d+) ' + c, s)
        if m:
            yield int(m.group(1))
        else:
            yield 0

def _parse(s):
    # "Game 1: 2 green, 12 blue; 6 red, 6 blue; 8 blue, 5 green, 5 red; 5 green, 13 blue; 3 green, 7 red, 10 blue; 13 blue, 8 red"
    s1, s2 = re.match(r'Game (\d+): (.*)', s).groups()
    return {
        "id": int(s1),
        "hands": [tuple(_parse_hand(x)) for x in s2.split('; ')]
    }

def solve01(input):
    it = (_parse(l) for l in input.splitlines())
    return sum(g["id"] for g in it if not any(any(map(operator.gt, h, BAG)) for h in g["hands"]))

def solve02(input):
    it = (_parse(l) for l in input.splitlines())
    return sum(math.prod(max(c) for c in zip(*g["hands"])) for g in it)

if __name__ == "__main__":
    input = data.get_input(2023, 2)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
