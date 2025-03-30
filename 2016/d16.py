from util import runner

def _batched(d):
    i = 0
    while i < len(d):
        yield (d[1], d[i+1])
        i += 2

def solve(size):
    data = "10001001100000001"
    while len(data) < size:
        next = "".join("1" if c == "0" else "0" for c in reversed(data))
        data = "0".join([data, next])
    data = data[:size]
    while len(data) % 2 == 0:
        data = "".join("1" if c1 == c2 else "0" for c1, c2 in _batched(data))
    return data

if __name__ == "__main__":
    runner.run(lambda: solve(272))
    runner.run(lambda: solve(35651584))
