#!/usr/bin/env python3

class Parent(object):
    """__best_fruit is initialized with mangling via __"""
    def __init__(self):
        self.__best_fruit = "Apples"

    def __method(self):
        """__method is mangled"""
        print(f'Hi, the parent fruit is {self.__best_fruit}')


class Child(Parent):
    """__best_fruit is initialized with mangling via __"""

    def __init__(self, fruit):
        self.__best_fruit = fruit

    def __method(self):
        '"""__method is mangled"""'
        print(f'Hi, the child fruit is {self.__best_fruit}')

#Note: The Parent Methods and variables have been mangled to prevent collision with the child

parent = Parent()
print(dir(parent))
assert "_method" not in dir(parent), "Name Mangling went wrong"
assert "_Parent__method" in dir(parent), "Name Mangling went wrong"
parent._Parent__method()


child = Child("Strawberrys")
print(dir(child))
assert "_method" not in dir(parent), "Name Mangling went wrong"
assert "_Child__method" in dir(child), "Name Mangling went wrong"
child._Child__method()
