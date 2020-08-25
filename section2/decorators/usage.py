
import time


def before_after(func):
    def wrapper(*args):
        print("Before")
        func(*args)
        print("After")

    return wrapper


class Test:
    # decorator can be used with a method
    @before_after
    def decorated_method(self):
        print("run")


t = Test()
t.decorated_method()
