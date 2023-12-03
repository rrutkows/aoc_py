from util import data, runner
from collections import defaultdict, deque
import re, math, itertools

class BotRule:
    # low and hight are tuples ('bot'|'output', value)
    def __init__(self, low, high):
        self.low = low
        self.high = high

def solve(input, part_one):
    bots = defaultdict(set)
    outputs = {}
    bot_rules = {}
    q = deque() # tuples (value, bot ID); value goes to bot
    for l in input.splitlines():
        # Parse:
        # value 5 goes to bot 2
        # bot 2 gives low to bot 1 and high to bot 0
        # bot 0 gives low to output 2 and high to output 0
        if m := re.match(r'value (\d+) goes to bot (\d+)', l):
            q.append(map(int, m.groups()))
        if m := re.match(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', l):
            bot_rules[int(m.group(1))] = BotRule((m.group(2), int(m.group(3))), (m.group(4), int(m.group(5))))
    while q:
        v, b = q.popleft()
        bots[b].add(v)
        if part_one and bots[b] == {61, 17}:
            return b
        if len(bots[b]) == 2:
            r = bot_rules[b]
            for v, r in zip(sorted(bots[b]), [r.low, r.high]):
                match r:
                    case ('output', id):
                        outputs[id] = v
                    case ('bot', id):
                        q.appendleft((v, id))
    return math.prod(outputs[o] for o in [0, 1, 2])

if __name__ == "__main__":
    input = data.get_input(2016, 10)
    runner.run(lambda: solve(input, True))
    runner.run(lambda: solve(input, False))
