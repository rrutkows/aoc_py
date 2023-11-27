import time, timeit, sys

def run(f):
    def format_time(t):
        units = [("s", 1.0), ("msec", 1e-3), ("us", 1e-6), ("ns", 1e-9)]
        for unit, scale in units:
            if t > scale:
                break

        return f"{t/scale:.3f} {unit}"


    if "-b" in sys.argv[1:]:
        timer = timeit.Timer(f)
        n, t = timer.autorange()
        print(format_time(t/n))
    else:
        start = time.perf_counter()
        result = f()
        end = time.perf_counter()
        print(result, format_time(end - start))
