# The _ prefix means stay away even if you're not technically prevented from doing so. You don't play around with another class's variables that look like __foo or _bar.

class A:
    def __init__(self):
        self.__var1 = 123
        self.var2 = 234

    def printVar(self):
        print(self.__var1)


a = A()
print(a.var2)
# print(a.__var1)
print(a.printVar())
