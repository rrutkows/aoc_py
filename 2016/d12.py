from util import data, runner

def _get_value(s, reg):
    if s in 'abcd':
        return reg[s]
    else:
        return int(s)

def solve(input, c):
    reg = dict(a = 0, b = 0, c = c, d = 0)
    instr = input.splitlines()
    i = 0
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
        i += d

    return reg['a']

if __name__ == "__main__":
    input = data.get_input(2016, 12)
    runner.run(lambda: solve(input, 0))
    runner.run(lambda: solve(input, 1))