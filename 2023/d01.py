from util import data, runner
import re

_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
_digits_alt = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e",
                "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}

def _to_digit(s):
    if s.isdigit():
        return s
    return str(_digits.index(s) + 1)

def solve01(input):
    it = (re.findall(r'\d', l) for l in input.splitlines())
    return sum(int(f"{x[0]}{x[-1]}") for x in it)

def solve02(input):
    p1 = re.compile('|'.join(_digits) + r'|\d')
    p2 = re.compile(r'.*(' + '|'.join(_digits) + r'|\d)')
    it = ((p1.search(l).group(), p2.search(l).group(1)) for l in input.splitlines())
    return sum(int(''.join((map(_to_digit, x)))) for x in it)

def solve02_alt(input):
    def replace(s):
        for k, v in _digits_alt.items():
            s = s.replace(k, v)
        return s
    it = (re.findall(r'\d', replace(l)) for l in input.splitlines())
    return sum(int(f"{x[0]}{x[-1]}") for x in it)

if __name__ == "__main__":
    input = data.get_input(2023, 1)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
    runner.run(lambda: solve02_alt(input))