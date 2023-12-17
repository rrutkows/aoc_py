from util import data, runner
from itertools import cycle
import math, re

_directions = dict(L = 0, R = 1)

def _parse(input):
    it = iter(input.splitlines())
    instructions = next(it)
    next(it)
    it = (re.findall(r'(\w+)', l) for l in it)
    nodes = {x[0]: (x[1], x[2]) for x in it}
    return (instructions, nodes)

def _find_path_lenght(start, end, nodes, instructions):
    id = start
    for i, d in enumerate(cycle(instructions)):
        id = nodes[id][_directions[d]]
        if id == end:
            return i + 1

def _find_cycle(start, nodes, instructions):
    id = start
    it = enumerate(cycle(instructions))
    for i, d in it:
        id = nodes[id][_directions[d]]
        if id[-1] == "Z":
            break
    cycle_start_id, cycle_start = id, i + 1
    for i, d in it:
        id = nodes[id][_directions[d]]
        if id[-1] == "Z":
            if id != cycle_start_id or i + 1 - cycle_start != cycle_start:
                raise RuntimeError("Complex cycles not supported")
            return cycle_start

def solve01(input):
    instructions, nodes = _parse(input)
    return _find_path_lenght('AAA', 'ZZZ', nodes, instructions)

def solve02(input):
    instructions, nodes = _parse(input)
    cycles = [_find_cycle(x, nodes, instructions) for x in nodes.keys() if x[-1] == "A"]
    return math.lcm(*cycles)

if __name__ == "__main__":
    input = data.get_input(2023, 8)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
