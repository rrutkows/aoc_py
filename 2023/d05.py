from util import data, runner
import re

def solve01(input):
    it = iter(input.splitlines())
    current = set(map(int, next(it).split(':')[1].split()))
    mapped = set()
    for l in it:
        if "map" in l:
            current.update(mapped) # return mapped
            mapped = set()
        elif l:
            d, s, r = tuple(map(int, l.split()))
            to_map = {n for n in current if n in range(s, s + r)}
            current -= to_map
            mapped.update(d + n - s for n in to_map)
    return min(current | mapped)

def solve02(input):
    it = (iter(input.splitlines()))
    current = set(tuple(map(int, pair)) for pair in re.findall(r'(\d+) (\d+)', next(it).split(':')[1]))
    mapped = set()
    for l in it:
        if "map" in l:
            current.update(mapped) # return mapped
            mapped = set()
        elif l:
            d, s, r = tuple(map(int, l.split()))
            to_map = {pair for pair in current if pair[0] < s + r and sum(pair) - 1 >= s}
            current -= to_map
            for ss, rr in to_map:
                mapped.add((d + max(s, ss) - s, min(s + r, ss + rr) - max(s, ss)))
                if rr > s + r - ss:
                    current.add((s + r, ss + rr - s - r)) # return unmapped remainder
                if ss < s:
                    current.add((ss, s - ss)) # return unmapped remainder
    return min(pair[0] for pair in current | mapped)

if __name__ == "__main__":
    input = data.get_input(2023, 5)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
