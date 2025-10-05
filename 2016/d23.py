from collections import deque
import re
from util import data, runner

def _get_value(s, reg):
    if s in 'abcd':
        return reg[s]
    else:
        return int(s)

def solve(input, a_start):
    reg = dict(a = a_start, b = 0, c = 0, d = 0)
    instr = input.splitlines()
    i = 0
    while i in range(len(instr)):
        a = instr[i].split()
        d = 1
        match a[0]:
            case 'cpy':
                if (a[2] in 'abcd'):
                    reg[a[2]] = _get_value(a[1], reg)
            case 'inc':
                reg[a[1]] = reg[a[1]] + 1
            case 'dec':
                reg[a[1]] = reg[a[1]] - 1
            case 'jnz':
                if _get_value(a[1], reg) != 0:
                    if i == 9:
                        reg['a'] = reg['a'] + reg['b'] * reg['d']
                        reg['c'] = 0
                        reg['d'] = 0
                    else:
                        d = _get_value(a[2], reg)
            case 'tgl':
                j = i + _get_value(a[1], reg)
                if j in range(len(instr)):
                    b = instr[j].split()
                    if len(b) == 2:
                        instr[j] = f"{'dec' if b[0] == 'inc' else 'inc'} {b[1]}"
                    if len(b) == 3:
                        instr[j] = f"{'cpy' if b[0] == 'jnz' else 'jnz'} {b[1]} {b[2]}"
        i += d

    return reg['a']

if __name__ == "__main__":
    input = data.get_input(2016, 23)
    runner.run(lambda: solve(input, 7))
    runner.run(lambda: solve(input, 12))