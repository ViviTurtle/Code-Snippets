Actual Useful Code Snippets
======
#### Sort Tuple or Dictionary by Value
```python
#Tuples
tuples = [(1,'w') , (2, 'e'), (3, 'a)')]
sorted(tuples, key=lambda x: x[1])

#Dicts
dict = {1: "Peter", 2:"Alice", 3:"Bob"}
sorted(dict.items(), key=lambda x: x[1])

```


Sort Dictionary by ther