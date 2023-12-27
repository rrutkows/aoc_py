from collections import defaultdict, namedtuple
from heapq import heapify, heappop, heappush
from util import data, runner

def _parse(input):
    bricks = []
    for l in input.splitlines():
        x = [int(n) for n in l.replace('~', ',').split(',')]
        start = x[:3]
        vec = [j - i for i, j in zip(x, x[3:])]
        if any(v<0 for v in vec):
            print(l)
        bricks.append((start, vec))
    return bricks

def _sort_by_z(bricks, *, reverse = False):
    return sorted(bricks, key = lambda b: b[0][2], reverse = reverse)

def _enum_xy(brick):
    for x in range(brick[0][0], brick[0][0] + brick[1][0] + 1):
        for y in range(brick[0][1], brick[0][1] + brick[1][1] + 1):
            yield x, y

def solve(input):
    bricks = _sort_by_z(_parse(input))
    stack = []
    zs = dict()
    may_destroy = set(range(len(bricks)))
    will_fall_counter = defaultdict(int)
    supported_by = [[] for _ in range(len(bricks))]

    def _increase_counter(brick_idx):
        q = [(-zs[i], i) for i in supported_by[brick_idx]]
        heapify(q)

        Seen = namedtuple('Seen', ['other_supporters', 'will_fall'])
        seen = {i: Seen({j for j in supported_by[brick_idx] if j != i}, set()) for i in supported_by[brick_idx]}

        while q:
            _, i = heappop(q)
            if not (seen[i].other_supporters - seen[i].will_fall):
                will_fall_counter[i] += 1
            for j in supported_by[i]:
                if not j in seen:
                    heappush(q, (-zs[j], j))
                    seen[j] = Seen(set(), set())
                seen[j].other_supporters.update(seen[i].other_supporters)
                seen[j].other_supporters.update(k for k in supported_by[i] if k != j)
                seen[j].will_fall.update(seen[i].will_fall)
                seen[j].will_fall.add(i)

    for i, brick in enumerate(bricks):
        z = brick[0][2]
        while z > 1:
            supporting = set()
            if len(stack) > z - 2:
                for x, y in _enum_xy(brick):
                    if (x, y) in stack[z - 2]:
                        supporting.add(stack[z - 2][(x, y)])
            if supporting:
                supported_by[i].extend(supporting)
                _increase_counter(i)
                if len(supporting) == 1:
                    may_destroy.discard(supporting.pop())
                break
            z -= 1
        zs[i] = z
        for brick_z in range(brick[1][2] + 1):
            if len(stack) < z + brick_z:
                stack.append(dict())
            for x, y in _enum_xy(brick):
                stack[z + brick_z - 1][(x, y)] = i

    with open("d22.gv", mode='w') as f:
        print("digraph G {", file = f)
        for i, v in enumerate(supported_by):
            for j in v:
                print(f"  {i} -> {j};", file=f)
        for k, v in will_fall_counter.items():
            print(f"  {k}[shape=box,label=\"{k}: {v}\"];", file=f)
        print("}", file = f)

    return len(may_destroy), sum(will_fall_counter.values())

if __name__ == "__main__":
    input = data.get_input(2023, 22)
    runner.run(lambda: solve(input))
