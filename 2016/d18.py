from util import data, runner

def solve(input, rows):
    ans = 0
    for _ in range(rows):
        ans += input.count('.')
        temp = f'.{input}.'
        input = ''
        for j in range(len(temp) - 2):
            input += '^' if temp[j] != temp[j + 2] else '.'

    return ans

if __name__ == "__main__":
    input = data.get_input(2016, 18).splitlines()[0]
    runner.run(lambda: solve(input, 40))
    runner.run(lambda: solve(input, 400000))