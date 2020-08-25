def foo():
    print("hello")


def foo2(func):
    return func


def foo3(func):
    return func()


foo2(foo)  # nothing
foo3(foo)  # "hello"
