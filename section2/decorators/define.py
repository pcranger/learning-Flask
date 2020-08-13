# define a function that we will later implement

def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)
        print("Ended")

    return wrapper


@f1
def f(a, b, c):
    print(a, b, c)


f("hello", 9, 78)
# "@f1" == "f = f1(f)" f = f1 at f or x = f1 at f if x = f1(f)
# function aliasing
# everytime we call f it's actually gonna call f1 with f as parameter


def f2(func):
    def wrapper(*args, **kwargs):
        print("Started")
        # store func in var to return values from f2() to add()
        val = func(*args, **kwargs)
        print("Ended")
        return val
    return wrapper


@f2
def add(x, y):
    return x + y


print(add(4, 5))
