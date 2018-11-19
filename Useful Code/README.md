Actual Useful Code Snippets
======
### Sort Tuple or Dictionary by Value
```python
#Tuples
tuples = [(1,'w') , (2, 'e'), (3, 'a)')]
sorted(tuples, key=lambda x: x[1])

#Dicts
dict = {1: "Peter", 2:"Alice", 3:"Bob"}
sorted(dict.items(), key=lambda x: x[1])

```


### Decorators
Useful Decorators that contain the following:

1) [Runtime](Decorators/runtime.py)
    * Used to record the real-life run time of a function, useful when trying to figure out faster algorithms
2) [Thread](Decorators/thead.py)
    * Used to async thread a function
3) [Trace](Decorators/trace.py)
    * Prints the function being called and its return values - Useful for debugging call-trees or general function outputs
4) Logging (TODO)
    * Similar to trace but outputs the function, return, date time, and user of who is calling the function