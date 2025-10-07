from collections import deque
from itertools import count
import re
from util import data, runner

def _get_value(s, reg):
    if s in 'abcd':
        return reg[s]
    else:
        return int(s)

def xsolve(input):
    instr = input.splitlines()
    for a in count():
        if _try(instr, a, 0):
            return a

def solve(input):
    # First 8 lines just add 7 * 362 to registry a and store result in registry d.
    instr = input.splitlines()[8:]
    return next(iter(a for a in count() if _try(instr, a, a + 7 * 362)))

def _try(instr, a_start, d_start):
    reg = dict(a = a_start, b = 0, c = 0, d = d_start)
    i = 0
    last_out = None
    outs = 0
    while i in range(len(instr)):
        a = instr[i].split()
        d = 1
        match a[0]:
            case 'cpy':
                reg[a[2]] = _get_value(a[1], reg)
            case 'inc':
                reg[a[1]] = reg[a[1]] + 1
            case 'dec':
                reg[a[1]] = reg[a[1]] - 1
            case 'jnz':
                if _get_value(a[1], reg) != 0:
                    d = int(a[2])
            case 'out':
                if last_out != None and reg['b'] == last_out:
                    return False
                last_out = reg['b']
                outs += 1
                if outs == 10:
                    return True
        i += d

if __name__ == "__main__":
    input = data.get_input(2016, 25)
    runner.run(lambda: solve(input))
