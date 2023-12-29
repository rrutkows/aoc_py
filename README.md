Python solutions for https://adventofcode.com/

### Provide your input
The scripts download and cache input.
Get the value of AOC session cookie from the browser and put it (**without newline**) in a file `session` in the top level directory.

Exceptions:
* Y2016 D05: Paste your door ID in `2016.d05._get_hashes`.
* Y2023 D20: Incomplete. Read your input. Put the name of rx's input into `2023.d20.solve02`.
  Increase the iteration count, if necessary, until all rx's input's inputs are printed.
  Put the values of first occurrences of each input
  into [lcm](https://docs.python.org/3/library/math.html#math.lcm)
  to get the answer.
* Y2023 D22: A [Graphviz](https://graphviz.org/) visualization will be created in `d22.gv`.
* Y2023 D24: [Z3](https://github.com/Z3Prover/z3) is required.
  Install `python3-z3`, if you're on Debian.
* Y2023 D25: Incomplete. A Graphviz visualization will be created in `d25.gv`.
  The connections to cut will be clearly visible.
  Export the graph to SVG and use browser's dev console to highlight the connections
  and see connected components. Hardcode components' names to get the result.

### Run
Either
```
./run.sh YYYY D|DD
```
or
```
python3 -m YYYY.dDD
```
For example
```
./run.sh 2016 5
./run.sh 2023 11
./python3 -m 2023.d08
```

### Benchmark
There is a simple benchmark implemented with [timeit](https://docs.python.org/3/library/timeit.html).
Run the benchmark with either
```
./bench.sh YYYY D|DD
```
or
```
python3 -m YYYY.dDD -b
```
