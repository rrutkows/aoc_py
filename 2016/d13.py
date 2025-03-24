from collections import Counter, deque
from util import runner

def _wall(x, y):
    v = x*x + 3*x + 2*x*y + y + y*y + 1352
    return Counter(f"{v:b}")['1'] % 2 == 1

def solve01():
    q = deque([(0, (1, 1))])
    visited = {(1,1)}
    while q:
         steps, c = q.popleft()
         if c == (31, 39):
              return steps
         x, y = c
         for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
              if x + dx >= 0 and y + dy >=0 and not _wall(x + dx, y+dy) and (x + dx, y + dy) not in visited:
                   visited.add((x + dx, y + dy))
                   q.append((steps + 1, (x + dx, y + dy)))
    return -1

def solve02():
    q = deque([(0, (1, 1))])
    visited = {(1,1)}
    while q:
         steps, c = q.popleft()
         x, y = c
         if steps < 50:
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                if x + dx >= 0 and y + dy >=0 and not _wall(x + dx, y+dy) and (x + dx, y + dy) not in visited:
                    visited.add((x + dx, y + dy))
                    q.append((steps + 1, (x + dx, y + dy)))
    return len(visited)

if __name__ == "__main__":
    runner.run(solve01)
    runner.run(solve02)