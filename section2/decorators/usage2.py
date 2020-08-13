import time

# to measure execution time of a function


def timer(func):
    def wrapper(*args):
        before = time.time()
        func()
        print("Function took: ", time.time() - before, "seconds")
    return wrapper


@timer
def algo():
    time.sleep(2)


algo()
