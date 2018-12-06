Data Structure
=======

**Dictionary Based**

Trying to find the dictionary type to use for things such as?
* Immutable
* Ordered
* Combined Dictionaries 

*See [Dictionary](Dictionary)*


**List Based**

gTrying to find the best list to use for things such ass
* Immutable
* Space-efficient single data type C type array
* Byte specific List?

**Class Based**

These are classes that can be used as an alternative to making a full seperate class
> This is useful if you need a **self-documenting** class that only uses **getters and setters**

**Immutable Class /w set and get**
```python
###Python 2.6+
from collections import namedtuple
Pokemon = namedtuple("Pokemon",'name, level, type_1, type_2')
Charizard = Pokemon("Charizard", 52, "fire", "flying")
#>>> Charizard
#Pokemon(name='Charizard', level=52, type_1='fire', type_2='flying')
print(f'My pokemon\'s level is {Charizard.level}')

####Python 3.0+
from typing import NamedTuple
class Pokemon(NamedTuple):
    """ Same as above except python3 adds type hints"""
	name: str
	level: int
	type_1: str
	type_2: str

jigglypuff= Pokemon("Jigglypuff", 14, "normal", "N/A")
#>>> Charizard
```
