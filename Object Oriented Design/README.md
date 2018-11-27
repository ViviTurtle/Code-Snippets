Object Oriented Checklist
=====
This is used as a general checklist to ensure proper clean code

### \_\_repr__ and \_\_str__
All classes should have \_\_repre__() or \_\_str__() function to show the its values in REPL or Print statements

>Default: >>> fruits -> fruits at \<address>

>\__repr__(): >>> fruits --> fruit("apple", small...)

>\__str__(): >>> fruits -> The fruit is an apple



*see [reprstr](reprstr.py)*

### Private Classes, Methods, and Variables
Wildcard imports will **not** import **private classes only** (private variables/methods is just a convention) 

>How: Prepend _ to classes, methods, and variables i.e. _private_class(object):

*see [Private Class Example](Private)*


### Name Mangling 
**- Subclassing**

Subclassing may have overlap variables and method names. If Name Mangling is not used, child methods/variables will override the parents

>How: Prepend __ to methods and variables e.g. __var1, __method1()

*see [Name Mangling Example](name_mangling.py)*

**- Python Keyword Mangling**

Note: If Name mangling /w Python keywords just append a "_" character e.g.
> def method(self, class_):

### Operator Overloading
Anytime classes need to be compared to itself (Combining, diff, shifted, encoded), operator overloading can be used to simplify

*See [Operator Overloading](https://www.python-course.eu/python3_magic_methods.php)*

**Example:**
```python

 def __add__(self, other):
		l = self.Converse2Metres() + other.Converse2Metres()
		return Length(l / Length.__metric[self.unit], self.unit )]

```

### Unique Decorators

**Abstract Classes**

Abstract classes with abstract methods can be created in order to ensure certain functions are implemented when subclassed.

*Note: replace raise NotImplementedError() since it does not check during initiation*
```python
from abc import ABCMeta, abstractmethod

class MyAbstractClass(metaclass=ABCMeta):

	@abstractmethod
	def required_implementation(self):
		pass
		
	def inherited_methozd(self): 
		pass
```

### Class Variables
Class Variables can be used for **shared** variables across all instances of a class. E.g. When you want to see how many times a class has been instantitiated

*Note: Class variables are accessed via self.\__class\__.<var_name>*

*See [Class Variable Example](class_variables.py)*


### Factory Methods
Factory Methods can be implemented via **class methods**. Class Methods are similar to @staticmethods except that they have write access to the overall class

*See [Factory Method Example](factory_method.py)*