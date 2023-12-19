from math import prod
from itertools import takewhile
from util import data, runner

_MAX = 4000

def _invert(r):
    if r.start > 1:
        return range(1, r.start)
    return range(r.stop, _MAX + 1)

def _intersect(r1, r2):
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop))

def _replace(d, key, value):
    new = dict()
    for k, v in d.items():
        new[k] = value if k == key else v
    return new

def _parse(input):
    it = iter(input.splitlines())
    workflows_input = takewhile(lambda l: l, it)
    workflows = dict()
    for l in workflows_input:
        name, rules_input = l.split('{')
        rules = []
        for rule_input in rules_input[:-1].split(','):
            rule_parts = rule_input.split(':')
            if len(rule_parts) == 1:
                exit = rule_input
            else:
                category, op, value = rule_parts[0][0], rule_parts[0][1], int(rule_parts[0][2:])
                if op == '<':
                    rules.append((category, range(1, value), rule_parts[1]))
                elif op == '>':
                    rules.append((category, range(value + 1, _MAX + 1), rule_parts[1]))
        workflows[name] = (rules, exit)

    parts = [dict((x[0], int(x[2:])) for x in l[1:-1].split(',')) for l in it]
    return workflows, parts

def solve01(input):
    workflows, parts = _parse(input)
    result = 0
    for part in parts:
        workflow_id = "in"
        while workflow_id in workflows:
            rules, exit = workflows[workflow_id]
            for category, valid_range, workflow_id in rules:
                if part[category] in valid_range:
                    break
            else:
                workflow_id = exit
        if workflow_id == 'A':
            result += sum(part.values())
    return result

def solve02(input):
    workflows, _ = _parse(input)
    q = [("in", {category: range(1, _MAX + 1) for category in 'xmas'})]
    result = 0
    while q:
        workflow_id, ranges = q.pop()
        if workflow_id == 'A':
            result += prod(len(r) for r in ranges.values())
        elif workflow_id in workflows:
            rules, exit = workflows[workflow_id]
            for category, valid_range, workflow_id in rules:
                new_range = _intersect(valid_range, ranges[category])
                if new_range:
                    q.append((workflow_id, _replace(ranges, category, new_range)))
                old_range = _intersect(_invert(valid_range), ranges[category])
                if not old_range:
                    break
                ranges[category] = old_range
            else:
                q.append((exit, ranges))
    return result

if __name__ == "__main__":
    input = data.get_input(2023, 19)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
