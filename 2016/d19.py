from collections import deque
from util import runner

E = 3018458

def solve01():
    e = deque(range(E))
    while len(e) > 1:
        e.rotate(-1)
        e.popleft()
    return e[0]+1

def solve02():
    front = deque(range(E//2))
    back = deque(range(E//2, E))
    while front:
        back.popleft()
        back.append(front.popleft())
        if len(front) < len(back) - 1:
            front.append(back.popleft())
    return back[0] + 1

if __name__ == "__main__":
    runner.run(solve01)
    runner.run(solve02)
