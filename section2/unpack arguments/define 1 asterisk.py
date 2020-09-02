# 1. *args in function call
def sum(a, b):
    return a + b


# data as tuple
values = (1, 2)

s = sum(*values)

# unpacks the tuple into arguments of sum()


#2. *args in argument
def multiply(*args):
    print(args)  # (1,3,5) (args is a tuple)
    print(*args)  # 1 3 5    (*args is each individual parameters)


multiply(1, 3, 5)
# pack the arguments of multiply() to args
