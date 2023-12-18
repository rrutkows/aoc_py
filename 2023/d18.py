from util import data, runner

_directions = 'RDLU'

def _parse_p1(s):
    fragm = s.split()
    return fragm[0], int(fragm[1])

def _parse_p2(s):
    s = s.split()[-1]
    return _directions[int(s[-2])], int(s[2:-2], base = 16)

def solve(input, parse):
    y, area, length = 0, 0, 0
    it = (parse(l) for l in input.splitlines())
    for d, fragment_length in it:
        length += fragment_length
        match d:
            case 'R':
                area += fragment_length * y
            case 'L':
                area -= fragment_length * y
            case 'D':
                y += fragment_length
            case 'U':
                y -= fragment_length
    return abs(area) + length // 2 + 1

if __name__ == "__main__":
    input = data.get_input(2023, 18)
    runner.run(lambda: solve(input, _parse_p1))
    runner.run(lambda: solve(input, _parse_p2))
