## • Why indentation is so important in Python :snake:

Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

Python uses indentation to indicate a block of code, Python will give you an error if you skip the indentation

``` bash
if 5 > 2:
  print("Five is greater than two!")
```

### •	How to use the if, if ... else statements
Python supports the usual logical conditions from mathematics:
``` bash

•	Equals: a == b
•	Not Equals: a != b
•	Less than: a < b
•	Less than or equal to: a <= b
•	Greater than: a > b
•	Greater than or equal to: a >= b

```
#### If
An "if statement" is written by using the if keyword.

``` bash
If statement:
•	a = 33
b = 200
if b > a:
  print("b is greater than a")
```

#### Elif

The elif keyword is pythons way of saying "if the previous conditions
 were not true, then try this condition".
``` bash
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```

#### Else
The else keyword catches anything which isn't caught by the preceding conditions.
``` bash
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```

### •	How to use comments

Comments starts with a #, and Python will ignore them.
omments can be used to explain Python code.

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.
``` bash
#This is a comment
print("Hello, World!")
```
### •	How to affect values to variables
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
``` bash
x = 5
y = "John"
print(x)
print(y)
```
Variables do not need to be declared with any particular type and can even change type after they have been set.

### •	How to use the while and for loops

**The while Loop**

With the while loop we can execute a set of statements as long as a condition is true.
``` bash 
Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1
```
The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

**The For Loop**

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
``` bash
Example
Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

### •	How is Python’s for different from C‘s?

Is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

### •	How to use the break and continues statements
The continue Statement
With the continue statement we can stop the current iteration, and continue with the next:

``` bash
Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```

With the break statement we can stop the loop even if the while condition is true:

``` bash
Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```

### •	How to use else clauses on loops

With the else statement we can run a block of code once when the condition no longer is true:

``` bash
Print a message once the condition is false:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```
### •What does the pass statement do, and when to use it
**for** loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

``` bash
for x in [0, 1, 2]:
  pass
```

### •	How to use range

To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

``` bash
Using the range() function:
for x in range(6):
  print(x)
```
The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6).

The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3).