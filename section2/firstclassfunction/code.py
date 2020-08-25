# A first class function just means that functions can be passed as arguments to functions.


def calculate(*values, operator):
    return operator(*values)


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"


# We pass the `divide` function as an argument operator
result = calculate(20, 4, operator=divide)
print(result)
