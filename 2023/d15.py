from collections import defaultdict
from functools import reduce
from itertools import chain
from util import data, runner

def _h(s):
    return reduce(lambda acc, c: (acc + ord(c)) * 17 % 256, s, 0)

# (operation, label, focal length)
def _parse(s): 
    if s[-1] == '-':
        return ('-', s[:-1], None)
    return ('=', s[:-2], int(s[-1]))

def solve01(input):
    it = chain.from_iterable(l.split(',') for l in input.splitlines())
    return sum(map(_h, it))

def solve02(input):
    it = chain.from_iterable(l.split(',') for l in input.splitlines())
    it = map(_parse, it)
    boxes = defaultdict(dict) # dict's insertion order is preserved since Python 3.7.
    for op, label, fl in it:
        h = _h(label)
        match op:
            case '-':
                if label in boxes[h]:
                    del boxes[h][label]
            case '=':
                boxes[h][label] = fl
    return sum((i + 1) * (j + 1) * l for i, box in boxes.items() for j, l in enumerate(box.values()))

if __name__ == "__main__":
    input = data.get_input(2023, 15)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
