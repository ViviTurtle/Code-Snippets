List based Data Structures
=======
Checklist/Cheat Sheet for optimal Data structures to use

**list**
> Basic Default mutable list

**Tuples**

>**Immutable containers** - Use if you need something similar to a read-only list
```python
curr_memory= 'one', 'two', 'three'
>> curr_memory
#('one', 'two', 'three')

```
                                  
**array.array**

>C type of array - Holds a single data type - More **space efficient** 
```python
import array
#float array
magic_numbers=array.array('f', (3.14, 0.33, 0.01 ))
magic_numbers
#array('f', [3.140000104904175, 0.33000001311302185, 0.009999999776482582])
```
                    
**bytes**
> An **immmutable** container for bytes (0-256) - Useful when you need to store byte specific memory  - Useful if working with low level machine code, networking stacks etc...
Note: Data is stored in \x00 fashion

Note: The mutable version i called bytearray
```python
# list of all possible characters to check for when writing exploits
all_characters = bytes((i for i in range(256)))
>>> all_characters
#b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13...

filtered_characters = bytearray((i for i in range(256) if i not in  (1,2,32,17)))
filtered_characters[15] = 4
```