from functools import cache
from util import runner
import hashlib, itertools, re

@cache
def _key(n, stretch):
    k = hashlib.md5(f'jlmsuwbz{n}'.encode()).hexdigest()
    for i in range(stretch):
        k = hashlib.md5(k.encode()).hexdigest()
    return k

def solve(stretch):
    re3 = re.compile(r'(.)\1\1')
    found = 0
    for i in itertools.count():
        k = _key(i, stretch)
        is_key = False
        m = re3.search(k)
        if m != None:
            re5 = re.compile(m.group(1) * 5)
            for j in range(1000):
                if re5.search(_key(i + j + 1, stretch)) != None:
                    is_key = True
                    break
        if is_key:
            found += 1
            if found == 64:
                return i
    return -1

if __name__ == "__main__":
    runner.run(lambda: solve(0))
    runner.run(lambda: solve(2016))
