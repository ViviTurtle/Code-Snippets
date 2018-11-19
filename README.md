Snippets
======

**This is a repository of reusable code**


General Checklist
====
This is used as a general checklist to ensure proper projects are being managed

### Asserts
Asserts should be used for **non-logic** conditionals to assist during runtime debugging

**Example:**
```python
assert 0 <= price <= product[price], "Impossible Discount for Price found"
```

### Unpacking iterables
When passing on a tuple, list, or dictionary to a function that takes on seperate arguments, you can simply use packing 
and unpacking features of python

*Note: Use ** when Unpacking keyword arguments*

**Example:**
```python
current_car = {"color": "tan", "mileage":92314, "make":"Toyota", "model": "prius", "year": 2011}
new_car = {"color": "red", "mileage":0, "make":"Toyota", "model": "prius", "year": 2018}
def buy_car(new_color, new_mileage, new_make, new_model, new_year):
    current_car["color"] = new_color
    current_car["mileage"] = new_mileage
    current_car["make"] = new_make
    current_car["model"] = new_model
    current_car["year"] = new_year

#Note that although we defined this function with more than more argument, we unpacked new_car into this function
buy_car(*new_car.values())
```
    
Conventions
=========
Mostly Syntax Clean code issues here

### Printing Strings (For Readability)
>Note: All these methods support format specification to format into decimal, hex, string...

*See https://docs.python.org/2.4/lib/typesseq-strings.html*

**- Python 3 and 2.7**
```python
print "The good guy is {good_guy} and the bad guy is {bad_guy}".format(good_guy = "Alice", bad_guy = "Bob")
```
**- Python 3.6+**
```python
>>> good_guy = "Alice"
>>> favorite_drink = 50159747054
>>> print(f'The good guy is {good_guy} and they are drinking {favorite_drink:x}')
The good guy is Alice and they are drinking badc0ffee

>>> print(f'3+4 is equal to {3+4}')
3+4 is equal to 7

```

### Python Comma Placement
Lists/Dicts should have a comma at the end of each line to help fix issues with missing commas in lists
```python
#This is a valid list (note the comma at the end of strawberry)
fruits = [
    "apples",
    "orange",
    "strawberries",
]
```

### Useless Placeholder "_" (Convention)
Use the _ character for useless placeholders
```python
#Repeat Hi 32 times
for _ in range(32):
    print "Hi"
    
#Last expression in REPL
>>> 14+4
18
>>> _
18

```


### Return None
By Default, all functions return None even if **not** explicitly written
```python
#The following functions are exactly the same
def none_v1():
    """Returns None everytime"""
    if (1 > 2):
        return "This will never happen"
        
def none_v2():
    """Returns None everytime"""
    if (1 > 2):
        return "This will never happen"
    return None

def none_v3():
    """Returns None everytime"""
    if (1 > 2):
        return "This will never happen"
    else:
        return None
        
```

