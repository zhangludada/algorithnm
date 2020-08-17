import time


def run_time(func):
    def tmp(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print(round(end - start, 4))

    return tmp
