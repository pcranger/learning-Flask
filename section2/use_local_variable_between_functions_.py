# 1. using return statement
def foo():
    a = 69
    return a


def foo2(func):
    print(func())


foo2(foo)
# 2. defining a class and make variable accessable to all methods(member)
