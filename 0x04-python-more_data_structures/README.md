## What are set and how to use them
A set is a collection which is unordered and unindexed.
 
A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).
 
However, a set itself is mutable. We can add or remove items from it.
 
>Note: Sets are unordered, so you cannot be sure in which order the items >will appear.
 
Like other collections, sets support x in set, len(set), and for x in set. Being an unordered collection, sets do not record element position or order of insertion. Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.
 
Operations: 
<img src=”https://www.google.com/url?sa=i&url=https%3A%2F%2Fpython-orientation.blogspot.com%2F2015%2F02%2Fpython-sets-and-dictionaries.html&psig=AOvVaw3AKGLkEhqdeSw18DjHyrsm&ust=1599836277625000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCIDjnNzs3usCFQAAAAAdAAAAABAJ”>
 
 
## What are dictionary and how to use them
A python dictionary is an unordered collection of items. It contains data as a set of key: value pairs.
 
Python allows the values in a dictionary to be any type – string, integer, a list, another dictionary, boolean, etc. However, keys must always be an immutable data type, such as strings, numbers, or tuples.
> If the key already exists, the old value will be overwritten.
> Performing list(d.keys()) on a dictionary returns a list of all the keys used > in the dictionary, in arbitrary order (if you want it sorted, just use 
> sorted(d.keys()) instead).  
> To check whether a single key is in the dictionary, use the in keyword.
 
What is a lambda function
lambda arguments: expression
This function can have any number of arguments but only one expression, which is evaluated and returned.
One is free to use lambda functions wherever function objects are required.
You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
It has various uses in particular fields of programming besides other types of expressions in functions.
 
## What is map, reduce and map functions
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
``` bash
Syntax :
map(fun, iter)
```
___
