Python solutions for https://adventofcode.com/

### Provide your input
The scripts download and cache input.
Get the value of AOC session cookie from the browser and put it (**without newline**) in a file `session` in the top level directory.

Exceptions:
* Y2016 D05: Paste your door ID in `2016.d05._get_hashes`.

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
