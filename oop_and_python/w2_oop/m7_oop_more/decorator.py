import math
import time


def timer(func):
    def inner(*args, **kargs):
        start = time.time()
        print("time started")
        print(args, kargs)
        func(*args, **kargs)
        end = time.time()
        print(f"time take: {end - start}")

    return inner


# vajilla way to decorate
# timer(get_factorial)()

# timer()()


@timer
def get_factorial(n):
    print("factorial starting")
    result = math.factorial(n)
    print(f"factorial of {n} is: {result}")


get_factorial(n=12)
