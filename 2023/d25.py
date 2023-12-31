from collections import defaultdict, deque
from util import data, runner

def _count(nodes, cut):
    start = next(iter(nodes.keys()))
    q = deque([start])
    seen = {start}
    while q:
        current = q.popleft()
        for node in nodes[current]:
            if node not in seen \
               and (current, node) not in cut \
               and (node, current) not in cut:
                q.append(node)
                seen.add(node)
    return len(seen)


def solve(input):
    nodes = defaultdict(set)
    parts = set()
    for l in input.splitlines():
        left, right = l.split(': ')
        nodes[left].update(right.split())
        parts.add(left)
        for r in right.split():
            nodes[r].add(left)
            parts.add(r)

    with open("d25.gv", mode='w') as f:
        print("graph G {", file = f)
        seen = set()
        for i, v in nodes.items():
            for j in v:
                if not (i, j) in seen:
                    print(f"  {i} -- {j};", file=f)
                    seen.add((j, i))
        print("}", file = f)

    cut = {('lsv', 'lxt'), ('ptj', 'qmr'), ('dhn', 'xvh')}
    count = _count(nodes, cut)
    return count * (len(parts) - count)

if __name__ == "__main__":
    input = data.get_input(2023, 25)
    runner.run(lambda: solve(input))
