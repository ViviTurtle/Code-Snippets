Object Oriented Checklist
=====
This is used as a general checklist to ensure proper clean code

### Private Classes, Methods, and Variables
Wildcard imports will **not** import **private classes only** (private variables/methods is just a convention) 

>How: Prepend _ to classes, methods, and variables i.e. _private_class(object):

*see [Private Class Example](Private)*


### Variable Name Mangling 
**- Subclassing**

Subclassing may have overlap variables and method names. If Name Mangling is not used, child methods/variables will override the parents

>How: Prepend __ to methods and variables e.g. __var1, __method1()

*see [Name Mangling Example](NameMangling)*

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

 
