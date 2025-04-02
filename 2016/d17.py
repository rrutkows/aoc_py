import hashlib
from collections import deque
from util import runner

_d = [(0, -1, 'U'), (0, 1, 'D'), (-1, 0, 'L'), (1, 0, 'R')]

def _h(path):
    p = 'edjrjqaa'
    return hashlib.md5(f'{p}{path}'.encode()).hexdigest()[:4]

def solve():
    W = 4
    H = 4
    shortest_path = None
    longest_path_length = 0
    q = deque([(0, 0, '')])  # Q el is (x, y, path)
    while q:
        x, y, path = q.popleft()
        if x == W - 1 and y == H - 1:
            if shortest_path is None:
                shortest_path = path
            if len(path) > longest_path_length:
                longest_path_length = len(path)
            continue
        h = _h(path)
        for i, (dx, dy, d) in enumerate(_d):
            nx = x + dx
            ny = y + dy
            if h[i] in 'bcdef' and nx in range(W) and ny in range(H):
                q.append((nx, ny, path + d))

    return shortest_path, longest_path_length

if __name__ == "__main__":
    runner.run(solve)
