# **kwargs as a parameter will pack argument to a dictionary
# kwarg is a dictionary
def test(**kwargs):
    print(kwargs)


test(name="bob", age=25)
