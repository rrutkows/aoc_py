from util import data, runner
import re

def _is_tls(s):
    if re.search(r'\[[^]]*(.)(?!\1)(.)\2\1', s):
        return False
    return re.search(r'(.)(?!\1)(.)\2\1', s)

def _get_babs(s):
    hypernet = False
    for i, c in enumerate(s):
        if hypernet:
            if c == ']':
                hypernet = False
        elif c == '[':
            hypernet = True
        else:
            aba_match = re.match(r'(.)(?!\1)([^[])\1', s[i:])
            if aba_match:
                a, b = aba_match.groups()
                yield f"{b}{a}{b}"

def _is_ssl(s):
    for bab in _get_babs(s):
        if re.search(r'\[[^]]*' + re.escape(bab), s):
            return True

def solve(input, check):
    return sum(1 for x in input.splitlines() if check(x))

if __name__ == "__main__":
    input = data.get_input(2016, 7)
    runner.run(lambda: solve(input, _is_tls))
    runner.run(lambda: solve(input, _is_ssl))
