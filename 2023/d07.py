from util import data, runner
from collections import Counter
from itertools import chain, islice

_cards = "AKQJT98765432"

_cards_p2 = "AKQT98765432J"

def _parse(h):
    c = Counter(h)
    l = list(x[1] for x in c.most_common())
    match l:
        case [5, *_]:
            return '7'
        case [4, *_]:
            return '6'
        case [3, 2, *_]:
            return '5'
        case [3, 1, *_]:
            return '4'
        case [2, 2, *_]:
            return '3'
        case [2, 1, *_]:
            return '2'
        case [1, *_]:
            return '1'

def _parse_p2(h):
    # Replace Js for most common non-J.
    for c, _ in Counter(h).most_common():
        if c != 'J':
            return _parse(h.replace('J', c))
    return _parse(h)

def _translate(h, parse, cards):
    # Translate 2 to 'A', 3 to 'B', ... A to 'O'
    # Put hand's strenth (1-7) in front.
    # The translation is sortable according to game's rules.
    it = (chr(ord('A') + len(cards) - 1 - cards.index(c)) for c in h)
    return ''.join(chain(parse(h), it))

def solve(input, parse, cards):
    it = iter(l.split() for l in input.splitlines())
    it = ((_translate(h, parse, cards), int(b)) for h, b in it)
    weak_to_strong = sorted(it, key = lambda pair: pair[0])
    return sum(pair[1] * (i + 1) for i, pair in enumerate(weak_to_strong))

if __name__ == "__main__":
    input = data.get_input(2023, 7)
    runner.run(lambda: solve(input, _parse, _cards))
    runner.run(lambda: solve(input, _parse_p2, _cards_p2))
