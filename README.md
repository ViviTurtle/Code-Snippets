Snippets
======

**This is a repository of reusable code**


SDLC Checklist
====
This is used as a general checklist to ensure proper projects are being managed
#### Asserts
Asserts should be used for **non-logic** conditionals to assist during runtime debugging

**Example:**
```python
assert(0 <= price <= product[price], "Impossible Discount for Price found")
```


Conventions
=========
Mostly Syntax Clean code issues here

#### Printing Strings (For Readability)
>Note: All these methods support format specification to format into decimal, hex, string...

*See https://docs.python.org/2.4/lib/typesseq-strings.html*

**- Python 3 and 2.7**
```python
print "The good guy is {good_guy} and the bad guy is {bad_guy}".format(good_guy = "Alice", bad_guy = "Bob")
```
**- Python 3.6+**
```python
good_guy = "Alice"
favorite_drink = 50159747054
print(f'The good guy is {good_guy} and they are drinking {favorite_drink:x}')
The good guy is Alice and the bad guy is Bob

>>> print(f'3+4 is equal to {3+4}')
3+4 is equal to 7

```

#### Python Comma Placement
Lists/Dicts should have a comma at the end of each line to help fix issues with missing commas in lists
```python
#This is a valid list (note the comma at the end)
fruits = [
    "apples",
    "orange",
    "strawberries",
]
```

#### Useless Placeholder "_" (Convention)
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
