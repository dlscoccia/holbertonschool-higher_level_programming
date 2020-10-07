0x0B. :snake: - Input/Output

#### How to open a file

The global open() function opens a file and returns a file object. In this case, the file we’re opening contains the pattern strings for pluralizing nouns. The with statement creates what’s called a context: when the with block ends, Python will automatically close the file, even if an exception is raised inside the with block
```
Syntax:
f = open("demofile.txt")
f = open("demofile.txt", "rt")
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
```


#### How to write text in a file
To write to an existing file, you must add a parameter to the open() function:

    "a" - Append - will append to the end of the file

    "w" - Write - will overwrite any existing content
```
>>> f = open("my_file_0.txt", "w")
>>> f.write("Now the file is ready to go!")
28
>>> f = open("my_file_0.txt", "r")
>>> print(f.read())
Now the file is ready to go!
>>>
```

#### How to read the full content of a file

The read() method allows us to read the full content of a file, like this:
      ```
      f = open("demofile.txt", "r")
      print(f.read())
      How to read a file line by line
      ```

By default the read() method returns the whole text, but you can also specify how many characters you want to return:
You can return one line by using the readline() method
By looping through the lines of the file, you can read the whole file, line by line:

    ```
    f = open("demofile.txt", "r")
    for x in f:
        print(x)
    ```

#### How to move the cursor in a file

In Python, seek() function is used to change the position of the File Handle to a given specific position. File handle is like a cursor, which defines from where the data has to be read or written in the file.

#### What is and how to use the with statement
with statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams.

There is nothing special in open() which makes it usable with the with statement and the same functionality can be provided in user defined objects. Supporting with statement in your objects will ensure that you never leave any resource open.

To use with statement in user defined objects you only need to add the methods __enter__() and __exit__() in the object methods. 
Consider the following example for further clarification.
```
# a simple file writer object 
class MessageWriter(object): 
	def __init__(self, file_name): 
		self.file_name = file_name 
	def __enter__(self): 
		self.file = open(self.file_name, 'w') 
		return self.file
	def __exit__(self): 
		self.file.close() 
# using with statement with MessageWriter 
with MessageWriter('my_file.txt') as xfile: 
	xfile.write('hello world') 
```
#### What is JSON
JSON stands for JavaScript Object Notation, is a lightweight format for storing and transporting data

#### What is serialization
In Python, when we want to serialize and de-serialize a Python object, we use functions and methods from the module Python Pickle. Pickling, then, is the act of converting a Python object into a byte stream. We also call this ‘serialization’, ‘marshalling’, or ‘flattening’. Unpickling is its inverse, ie., converting a byte stream from a binary file or bytes-like object into an object. 

Lets start with comparing Python serialize with other modules of Python.


#### How to convert a Python data structure to a JSON string, and viceversa.

If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

```
import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

Output:
{"name": "John", "age": 30, "city": "New York"}
```

