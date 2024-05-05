'''
### Why Python?
It is high-level, general-purpose, interpreted, dynamic, and object-oriented.

Two kinds of programs to process high-level languages into  low-level languages:
Intepreter: source code > interpreter > output (what python uses)
Compilers: sc > compiler > object code > executor > output

Compliler is like translating a book, Interpreter is like translating it line by line.
**Debugging with Python is easy as it simply raises an exception

"python" (command line argument ex: file)

Two ways to use the Python Interpreter:
Shell Mode: Typing direct python commands
Program Mode: Typing python into file and having interpreter read that (what this class uses)

### Some Basics
Immutable objects can not be updated in place. Instead, a new one is created and they are assigned. (New Memory Allocation)
Mutable objects can be updated in place. They retain their memory id: array, list, dict, set, and user defined classes

List Append (.append()) vs. Concatenate (+):
When appending, we are adding to the original list.
When concatenating, it will create an entirely new list.

Sequence Traversal:
By item
-> for (item) in items:
By index
-> for i in range(len(items)):

"empty" key word

Aliasing occurs when two or more variables reference the same object.
We can prevent aliasing by using slicing [:] or .copy()

### Memory blocks
Strings, Ints, etc. use one memory block
Lists use a memory block PER space

Equals (==) and is conditional:
== checks if values are similar
is checks if memory blocks are the same

Some useful methods:
.find(substr)
.replace(old, new)
.split()
"".join()

.upper() > switches to upper
.isupper() > checks if upper
.isdigit() > checks if all digit

.startswith(substr)
.endswith(substr)

In String with Min and Max functions, Uppercase COMES BEFORE Lower Case (Z < B)

.extend(iterable) to add a list to a list

.isinstance(item, *type) # checks typing

## Dicts
Use del to delete a key in dict
Use in to test for existence of a key
.keys()
.values()

.get() vs bracket[] for key: brackets might raise exception if key does not exist

'''