## 0x02. :snake: - import & modules
### :speech_balloon: How to import functions from another file
_Approach:_

1.- Create a Python file containing the required functions.

2.- Create another Python file and import the previous Python file into it.

3.- Call the functions defined in the imported file.
``` bash
# function
def displayText():
	print( "Import Function!")
```
``` bash
# importing all the  functions defined in test.py
from test import *

# calling functions
displayText()
```


### :speech_balloon: How to use imported functions
If a new file called myfunctions.py is created and contains two function definitions, plustwo() and falldist(), the functions plustwo() and falldist() can be used by a separate script as long as the file and function names are imported in the separate script first.

It is essential that the file which contains the function definitions ends in the .py extension. Without a .py extension, the file where the functions are defined can not be imported. Inside the file myfuctions.py, two functions are defined using the code below.


**Remember the file that contains the function definitions and the file calling the functions must be in the same directory.**


The general syntax to import and call a function from a separate file is below:


``` bash
from function_file import function_name

function_name(arguments)


from myfunctions import plustwo
plustwo(3)
```
> To import a variable from another file:
> ``` bash
> import filename.py
> print(filename.variable_name)
> ```
### :speech_balloon: How to create a module

Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter.

Such a file is called a module; definitions from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode).

### :speech_balloon: How to use the built-in function dir()

1.- The dir() function returns all properties and methods of the specified object, without the values.
This function will return all the properties and methods, even built-in properties which are default for all object.
2.- The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings
``` bash
dir(object)
```

#### Return Value from dir()

dir() tries to return a list of valid attributes of the object.
If the object has __dir__() method, the method will be called and must return the list of attributes.


If the object doesn't have __dir__() method, this method tries to find information from the __dict__ attribute (if defined), and from type object. In this case, the list returned from dir() may not be complete.


If an object is not passed to __dir()__ method, it returns the list of names in the current local scope.


### :speech_balloon: How to prevent code in your script from being executed when imported
One way to do this is to add if __name__ == '__main__': before the section of the module you do not want to be executed if it’s being imported.


The Python interpreter reads the source code of a module and executes everything in it from top to bottom. But before executing the code, it sets a few special variables, one of them is __name__. If the interpreter is running the file as the main program, it sets the __name__variable to '__main__'.


To prevent execution from happening during import we can write a conditional statement using __name__ and '__main__':
``` bash
#!/usr/bin/python3
If __name__ == “__main__”:
	X = 1
	print(x)
```
#### :speech_balloon: How to use command line arguments with your Python programs
Python provides a getopt module that helps you parse command-line options and arguments.
``` bash
$ python test.py arg1 arg2 arg3
```

The Python sys module provides access to any command-line arguments via the sys.argv. This serves two purposes −
sys.argv is the list of command-line arguments.
len(sys.argv) is the number of command-line arguments.

The use of Python command line arguments is also strongly influenced by the C language.
``` bash
# main.py
import sys

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
```
You don’t see an argc variable like in the C code example. It doesn’t exist in Python because sys.argv is sufficient. You can parse the Python command line arguments in sys.argv without having to know the length of the list, and you can call the built-in len() if the number of arguments is needed by your program.
> support for all Python command line arguments is provided by sys.argv.

Also, note that enumerate(), when applied to an iterable, returns an enumerate object that can emit pairs associating the index of an element in sys.arg to its corresponding value. This allows looping through the content of sys.argv without having to maintain a counter for the index in the list.

_____________________________________________________________________
Glosary:
1.- __import__: Imports a module.
``` bash
__import__(name, globals=None, locals=None, fromlist=(), level=0)
```