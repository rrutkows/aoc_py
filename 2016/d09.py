from util import data, runner
import re

def _decompress(s):
    i, result = 0, 0
    while i < len(s):
        m = re.match(r'\((\d+)x(\d+)\)', s[i:])
        if m:
            chars, times = map(int, m.groups())
            result += chars * times
            i += m.end() + chars
        else:
            i, result = i + 1, result + 1
    return result

def _decompress_v2(s):
    result, i, end = 0, 0, len(s)
    stack = []
    while i < end:
        m = re.match(r'\((\d+)x(\d+)\)', s[i:])
        if m:
            chars, times = map(int, m.groups())
            stack.append((result, times, end))
            result, i, end = 0, i + m.end(), i + m.end() + chars
        else:
            result, i = result + 1, i + 1
        while i == end and stack:
            tmp = stack.pop()
            result, end = tmp[0] + result * tmp[1], tmp[2]
    return result

def solve(input, decompress):
    return sum(decompress(l) for l in input.splitlines())

if __name__ == "__main__":
    input = data.get_input(2016, 9)
    runner.run(lambda: solve(input, _decompress))
    runner.run(lambda: solve(input, _decompress_v2))
