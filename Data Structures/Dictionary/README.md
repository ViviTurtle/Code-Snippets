Data Structure
=======
Checklist/Cheat Sheet for optimal Data structures to use

**Dictionary**

Default when needing a key:value mapping

>Note: Uses \__hash\__() dunder function to index the data structure*
```python
##All dictionaries
fruits = {"apple": "red", "orange": "orange", "banana": "yellow"}
empty_zoo = dict()
mult_7 = {x: x * 7 for x in (1,100)}
```


**Ordered Dictionary**

Used when need to preserve order of dictionary - might be useful when for **dictionary based stacks/queues**
```python
import collections
job_interview_schedule= collections.OrderedDict(tom="it support", adam="engineer", alice="sr. engineer")
print(job_interview_schedule)
print(job_interview_schedule.keys())
```

**Default Dict**

Useful when using a Dictionary values have a **default class** such Person() or list()

>Note: This can be used to make readability better of nested data structures such as a dictionary of lists

```python
import collections
employees=collections.defaultdict(list)
employees["IT"].append("Adam")
employees["IT"].append("Bob")
employees["IT"].append("Alice")
employees["HR"].append("Mary")
employees["HR"].append("Samantha")
employees["HR"].append("Will")
print(employees)
```

**Chain Map**

Need to access combine 2+ different dictionaries - Use Chain map
> PR THIS WITH WORK LAPTOP         
```python

```

                                                                                                                   