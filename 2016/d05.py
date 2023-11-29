from util import runner
import hashlib, itertools, re

def _get_hashes():
    return (hashlib.md5(f"ugkcyxxp{x}".encode()).digest().hex() for x in itertools.count())

def solve01():
    password = (x[5] for x in _get_hashes() if x[:5] == '00000')
    return ''.join(itertools.islice(password, 8))

def solve02():
    matches = (re.match(r'00000([0-7])(.)', x) for x in _get_hashes())
    matches = (x.groups() for x in matches if not x is None)
    visited = set()
    pwd = list(('0' for _ in range(8)))
    for pos, c in matches:
        if pos in visited:
            continue
        visited.add(pos)
        pwd[int(pos)] = c
        if len(visited) == 8:
            break
    return ''.join(pwd)

if __name__ == "__main__":
    runner.run(solve01)
    runner.run(solve02)