from collections import defaultdict, deque
from itertools import count
from math import prod
from util import data, runner

class Module:
    def __init__(self, outputs):
        self.outputs = outputs

    def receive(self, src, pulse):
        pass

class Broadcaster(Module):
    def __init__(self, outputs):
        Module.__init__(self, outputs)
    
    def receive(self, src, pulse):
        return pulse

class FlipFlop(Module):
    def __init__(self, outputs):
        Module.__init__(self, outputs)
        self._on = False

    def receive(self, src, pulse):
        if not pulse:
            self._on = not self._on
            return self._on
        return None

class Conjunction(Module):
    def __init__(self, inputs, outputs):
        Module.__init__(self, outputs)
        self._inputs = {i: False for i in inputs}

    def receive(self, src, pulse):
        self._inputs[src] = pulse
        return not all(self._inputs.values())

def _parse(input):
    inputs = defaultdict(list)
    for l in input.splitlines():
        module_input, outputs_input = l.split(' -> ')
        module_name = module_input[1:] if module_input[0] in '%&' else module_input
        for output in outputs_input.split(', '):
            inputs[output].append(module_name)

    modules = dict()
    for l in input.splitlines():
        module_input, outputs_input = l.split(' -> ')
        outputs = outputs_input.split(', ')
        if module_input[0] == '%':
            modules[module_input[1:]] = FlipFlop(outputs)
        elif module_input[0] == '&':
            modules[module_input[1:]] = Conjunction(inputs[module_input[1:]], outputs)
        elif module_input == 'broadcaster':
            modules[module_input] = Broadcaster(outputs)
    return modules

def solve01(input):
    modules = _parse(input)
    pulse_count = {True: 0, False: 0}
    for _ in range(1000):
        # print()
        q = deque([(False, 'button', 'broadcaster')])
        while q:
            pulse, src, dst = q.popleft()
            # print(f"{src} {'high' if pulse else 'low'} -> {dst}")
            pulse_count[pulse] += 1
            if dst in modules:
                next_pulse = modules[dst].receive(src, pulse)
                if next_pulse is not None:
                    q.extend((next_pulse, dst, next_dst) for next_dst in modules[dst].outputs)
    return prod(pulse_count.values())

def solve02(input):
    modules = _parse(input)
    for i in range(5000):
        q = deque([(False, 'button', 'broadcaster')])
        while q:
            pulse, src, dst = q.popleft()
            if dst == "qn" and pulse:
                print(f"{i + 1} {src} {'high' if pulse else 'low'} -> {dst}")
            if dst in modules:
                next_pulse = modules[dst].receive(src, pulse)
                if next_pulse is not None:
                    q.extend((next_pulse, dst, next_dst) for next_dst in modules[dst].outputs)

if __name__ == "__main__":
    input = data.get_input(2023, 20)
    runner.run(lambda: solve01(input))
    runner.run(lambda: solve02(input))
