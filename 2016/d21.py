from functools import reduce
from util import data, runner

def scramble(p, cmd):
    return scramble_unscramble(p, cmd, False)

def unscramble(p, cmd):
    return scramble_unscramble(p, cmd, True)

def rotate(p, x, dir):
    x = x % len(p)
    return p[-x:] + p[:-x] if dir == 'right' else p[x:] + p[:x]

def scramble_unscramble(p, cmd, un):
    s = cmd.split()
    # swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.
    # swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the string).
    if s[0] == 'swap':
        if s[1] == 'position':
            x, y = sorted([int(s[2]), int(s[5])])
        else:
            x, y = sorted([p.index(s[2]), p.index(s[5])])
        return p[:x] + p[y] + p[x+1:y] + p[x] + p[y+1:]
    # rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.
    # rotate based on position of letter X means that the whole string should be rotated to the right based on the index of letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
    # 0, 1, 2, 3 -> 1, 3, 5, 7
    # 4, 5, 6, 7 -> 2, 4, 6, 0
    if s[0] == 'rotate':
        if s[1] == 'based':
            x = p.index(s[6])
            if un:
                x = [9, 1, 6, 2, 7, 3, 8, 4][x]
                dir = 'left'
            else:
                if x >= 4:
                    x += 1
                x += 1
                dir = 'right'
        else:
            x = int(s[2])
            dir = s[1]
            if un:
                dir = 'right' if dir == 'left' else 'left'
        return rotate(p, x, dir)
    #reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
    if s[0] == 'reverse':
        x, y = int(s[2]), int(s[4])
        return p[:x] + ''.join(reversed(p[x:y+1])) + p[y+1:]
    #move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.
    if s[0] == 'move':
        x, y = int(s[2]), int(s[5])
        if un:
            x, y = y, x
        if x < y:
            return p[:x] + p[x+1:y+1] + p[x] + p[y+1:]
        elif x > y:
            return p[:y] + p[x] + p[y:x] + p[x+1:]
        else:
            return p
    return p

def solve01(input):
    return reduce(scramble, input.splitlines(), 'abcdefgh')

def solve02(input):
    return reduce(unscramble, reversed(input.splitlines()), 'fbgdceah')

if __name__ == "__main__":
    input = data.get_input(2016, 21)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))