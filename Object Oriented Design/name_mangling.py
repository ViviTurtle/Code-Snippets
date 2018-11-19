#!/usr/bin/env python3

class Parent(object):
    """__best_fruit is initialized with mangling via __"""
    def __init__(self):
        self.__best_fruit = "Apples"

    def __method(self):
        """__method is mangled"""
        print(f'Hi, the parent fruit is {self.__best_fruit}')


    def override(self):
        """override is not mangled and will be overrided from child"""
        return 'Hi, I am from the parent and have not been overrided.'


class Child(Parent):
    """
    __best_fruit is initialized with mangling via __
    Note: Child inherits the Parent class
    """

    def __init__(self, fruit):
        self.__best_fruit = fruit

    def __method(self):
        '"""__method is mangled"""'
        print(f'Hi, the child fruit is {self.__best_fruit}')

    def override(self):
        """override is not mangled and will be overrided from child"""
        return 'Hi, I am from the child and overrided the parent.'

#Note: The Parent Methods and variables have been mangled to prevent collision with the child

### Parent Series ###
parent = Parent()
print(dir(parent))
assert "_method" not in dir(parent), "Name Mangling went wrong"
assert "_Child__method" not in dir(parent), "Name Mangling went wrong"
assert "_Parent__method" in dir(parent), "Name Mangling went wrong"
assert "override" in dir(parent), "Name Mangling went wrong"
assert parent.override() == "Hi, I am from the parent and have not been overrided."

parent._Parent__method()

### Child Series ###
child = Child("Strawberrys")
print(dir(child))
assert "_method" not in dir(child), "Name Mangling went wrong"
#Note Both Child and Parent methods are within the child
assert "_Child__method" in dir(child), "Name Mangling went wrong"
assert "_Parent__method" in dir(child), "Name Mangling went wrong"
#Note override has no seperate child/Parent methods
assert "override" in dir(child), "Name Mangling went wrong"
assert child.override() == "Hi, I am from the child and overrided the parent.", "rawr"
child._Child__method()
