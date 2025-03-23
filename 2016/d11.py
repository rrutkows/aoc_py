import re
from collections import deque
from itertools import combinations
from util import data, runner

def _is_ok(chips, generators):
    return not generators or all(c in generators for c in chips)

def _flatten(floors):
    return '$'.join('|'.join(','.join(sorted(x)) for x in floor) for floor in floors)

def _is_done(floors):
    return all(not chips and not generators for (chips, generators) in floors[:-1])

def _parse_floor(l):
    generators = re.findall(r'(\w+) generator', l)
    chips = re.findall(r'(\w+)-compatible microchip', l)
    return (set(chips), set(generators))

def solve(input, part2):
    floors = [_parse_floor(l) for l in input.splitlines()]
    if part2:
        for extra in ['elerium', 'dilithium']:
            floors[0][0].add(extra)
            floors[0][1].add(extra)

    q = deque([(0, 0, floors)])  # Q el is (moves made, elevator's floor number, floors)
    visited = {(0, _flatten(floors))} # visited el is (elevator's floor number, flatten(floors))
    while q:
        moves, elevator_floor, floors = q.popleft()
        if _is_done(floors):
            return moves
        chips, generators = floors[elevator_floor]

        for d in [1, -1]:
            if elevator_floor + d in range(len(floors)):
                for chip_count in range(3):
                    for generator_count in range(3 - chip_count):
                        if chip_count + generator_count > 0:
                            for chips_to_move in combinations(chips, chip_count):
                                for generators_to_move in combinations(generators, generator_count):
                                    chips1 = chips - set(chips_to_move)
                                    generators1 = generators - set(generators_to_move)
                                    chips2 = floors[elevator_floor + d][0] | set(chips_to_move)
                                    generators2 = floors[elevator_floor + d][1] | set(generators_to_move)
                                    if _is_ok(chips1, generators1) and _is_ok(chips2, generators2):
                                        new_floors = floors[:]
                                        new_floors[elevator_floor] = (chips1, generators1)
                                        new_floors[elevator_floor + d] = (chips2, generators2)
                                        h = _flatten(new_floors)
                                        if (elevator_floor + d, h) not in visited:
                                            visited.add((elevator_floor + d, h))
                                            q.append((moves + 1, elevator_floor + d, new_floors))
    return -1

if __name__ == "__main__":
    input = data.get_input(2016, 11)
    runner.run(lambda: solve(input, False))
    runner.run(lambda: solve(input, True))
