# class methods decorate the class
# Corey distinguishes between a regular method, class method, and a static method.
# """ Firstly, a regular method is the type of method that we are used to seeing since the start of OOP tutorials. It is accessible through both the class and the instance, which means that we can call for the method in both
# Employee.method()
# and
# emp_1.method()
# they automatically have the instance as the first positional argument, as self.

# Secondly, class methods are the type of method used when a method is not really about an instance of a class, but the class itself. To create a class method, just add '@classmethod' a line before creating the class method. The class is automatically the first argument to be passed in, and is represented as 'cls' instead of 'class'. This is because 'class' is already assigned to be something else in Python. There are 2 ways of using the class method as far as Corey has shown.
# First is modifying the class variable. Corey modified the 'raise_amount' class variable using a class method. Just remember that to access a class variable, we have to write 'cls.' before specifying the actual name. For example, as 'cls.raise_amount' as in the video.

# Second is making an alternative constructor. Sometimes people have information of their specific instances of the class available in a specific format. Corey shows an example of this where first and last names and pay are separated by a hyphen. Corey creates a class method that returns the class with the specific values passed in that are obtained by using split() method to the string passed in. User of the script can now automatically create a new instance without having to parse the string at '-'.
# Corey then moves on to cover static methods. Static methods are different from regular methods an class methods in that it doesn't have a class or instance that is automatically passed in as a firs positional argument. They can be created by adding '@staticmethod' a line before defining the method. These are methods that have a logical connection to the Class, but does not need a class or instance as an argument. Corey says that it is better to make sure we create a static method rather then class or regular method when we are sure that we don't make use of the class or instance within the method. """

import datetime


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    # class methods take care of different people with different amount of raise amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    # class methods take care of the additional format of names people have for example they have hyphens between their names

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'


first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))


# A class method is one that belongs to the class as a whole.
# It doesn't require an instance. Instead, the class will automatically be sent as the first argument. A class method is declared with the @classmethod decorator.


class Foo(object):
    @classmethod
    def hello(cls):
        print("hello from %s" % cls.__name__)


Foo.hello()
Foo().hello()

# On the other hand, an instance method requires an instance in order to call it, and requires no decorator. This is by far the most common type of method.


class Foo(object):
    def hello(self):
        print("hello from %s" % self.__class__.__name__)


Foo.hello()  # error
