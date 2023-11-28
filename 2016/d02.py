from util import data, runner
from functools import reduce

def solve01(input):
    directions = dict(U = (0, -1), D = (0, 1), L = (-1, 0), R = (1, 0))
    code = []
    for l in input.splitlines():
        x, y = 1, 1
        for dx, dy in (directions[c] for c in l):
            x = max(0, min(2, x + dx))
            y = max(0, min(2, y + dy))
        code.append(f"{y * 3 + x + 1}")
    return ''.join(code)

def solve02(input):
    directions = dict(U = 0, L = 1, D = 2, R = 3)
    keypad = {
        '1': '1131',
        '2': '2263',
        '3': '1274',
        '4': '4384',
        '5': '5556',
        '6': '25A7',
        '7': '36B8',
        '8': '47C9',
        '9': '9899',
        'A': '6AAB',
        'B': '7ADC',
        'C': '8BCC',
        'D': 'BDDD'
    }
    code = (reduce(lambda acc, c: keypad[acc][directions[c]], l, '5') for l in input.splitlines())
    return ''.join(code)

if __name__ == "__main__":
    input = data.get_input(2016, 2)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
