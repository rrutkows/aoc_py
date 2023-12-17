from util import data, runner

def _predict(v):
    if all(x == 0 for x in v):
        return 0
    d = [x - y for x, y in zip(v[1:], v)]
    return v[-1] + _predict(d)

def _predict_p2(v):
    if all(x == 0 for x in v):
        return 0
    d = [x - y for x, y in zip(v[1:], v)]
    return v[0] - _predict_p2(d)

def solve(input, predict):
    return sum(predict([int(x) for x in l.split()]) for l in input.splitlines())

if __name__ == "__main__":
    input = data.get_input(2023, 9)
    runner.run(lambda: solve(input, _predict))
    runner.run(lambda: solve(input, _predict_p2))
