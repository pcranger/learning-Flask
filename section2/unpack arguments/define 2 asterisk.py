# 1. **kwargs in function call

def named(name, age):
    print(name, age)


# data as dict
bob = {"name": "Bob", "age": 25}
named(**bob)

# and unpacks the dict into arguments of named()

#2. **kwargs in argument


def test(**kwargs):
    print(kwargs)  # kwargs in a dict


test(name="bob", age=25)  # 2 pairs with be packed into 1 dict
# pack the arguments of test) to kwargs
