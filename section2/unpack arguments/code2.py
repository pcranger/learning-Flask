def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwarg.items():
        print(f"{arg}: {value}")
