# 	How to use the Python interpreter :snake:

The Python interpreter is usually installed as /usr/local/bin/python on those machines where it is available; putting /usr/local/bin in your UNIX shell's search path makes it possible to start it by typing the command
```bash
python
```
The interpreter operates somewhat like the UNIX shell: when called with standard input connected to a tty device, it reads and executes commands interactively; when called with a file name argument or with a file as standard input, it reads and executes a script from that file.

A second way of starting the interpreter is **"python -c command [arg] ..."**, which executes the statement(s) in command, analogous to the shell's -c option. 

Since Python statements often contain spaces or other characters that are special to the shell, it is best to quote command in its entirety with double quotes.

Some Python modules are also useful as scripts. These can be invoked using **"python -m module [arg] ..."**, which executes the source file for module as if you had spelled out its full name on the command line.


## •	How to print text and variables using print

The simplest example of using Python print() requires just a few keystrokes:


```bash
>>> print()
```

You don’t pass any arguments, but you still need to put empty parentheses at the end, which tell Python to actually execute the function rather than just refer to it by name.

calling **print()** without arguments results in a blank line, which is a line comprised solely of the newline character.

The print statement has been replaced with a print() function, with keyword arguments to replace most of the special syntax of the old print statement.
The print statement can be used in the following ways :

```bash 
print("Good Morning")
print("Good", <Variable Containing the String>)
print("Good" + <Variable Containing the String>)
print("Good %s" % <variable containing the string>)
```
In Python, single, double and triple quotes are used to denote a string. Most use single quotes when declaring a single character. Double quotes when declaring a line and triple quotes when declaring a paragraph/multiple lines.

## •	How to use strings

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.


## •	What are indexing and slicing in Python

Slicing is indexing syntax that extracts a portion from a list. If a is a list, then a[m:n] returns the portion of a:
•	Starting with postion m
•	Up to but not including n
•	Negative indexing can also be used
Here’s an example:

```bash 
>>> a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a[2:5]
['bacon', 'tomato', 'ham']
>>> a[-5:-2]
['egg', 'bacon', 'tomato']
>>> a[1:4]
['egg', 'bacon', 'tomato']
>>> a[-5:-2] == a[1:4]
True
```

#### Omitting the first and/or last index:

>	Omitting the first index a[:n] starts the slice at the beginning of the list.

>	Omitting the last index a[m:] extends the slice from the first index m to the end of the list.

> Omitting both indexes a[:] returns a copy of the entire list, but unlike with a string, it’s a copy, not a reference to the same object.

**Here’s an example:**

```bash
>>> a
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a[:4]
['spam', 'egg', 'bacon', 'tomato']
>>> a[0:4]
['spam', 'egg', 'bacon', 'tomato']
>>> a[2:]
['bacon', 'tomato', 'ham', 'lobster']
>>> a[2:len(a)]
['bacon', 'tomato', 'ham', 'lobster']

>>> a
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a[:]
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a == a[:]
True
>>> a is a[:]
False

>>> s = 'mybacon'
>>> s[:]
'mybacon'
>>> s == s[:]
True
>>> s is s[:]
True
```
