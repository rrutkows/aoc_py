from util import data, runner
from collections import defaultdict
import itertools, re

def _get_most_common_letters(s):
    s = s.replace('-', '')
    letters = defaultdict(lambda: 0)
    count = [set() for _ in range(len(s))]
    for c in s:
        if letters[c] > 0:
            count[letters[c]].remove(c)
        letters[c] += 1
        count[letters[c]].add(c)
    return itertools.chain.from_iterable((sorted(x) for x in reversed(count)))

def _get_real_rooms(input):
    parsed = (re.match(r'(.*)-(\d+)\[(.*)\]', l).groups() for l in input.splitlines())
    return ((name, int(id)) for name, id, checksum in parsed if checksum == ''.join(itertools.islice(_get_most_common_letters(name), 5)))

def _rotate(c, times):
    if c == '-':
        return ' '
    return chr(ord('a') + (ord(c) - ord('a') + times) % 26)

def solve01(input):
    return sum(id for _, id in _get_real_rooms(input))

def solve02(input):
    for name, id in _get_real_rooms(input):
        decrypted = ''. join((_rotate(c, id) for c in name))
        if decrypted == 'northpole object storage':
            return id
    return -1

if __name__ == "__main__":
    input = data.get_input(2016, 4)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
