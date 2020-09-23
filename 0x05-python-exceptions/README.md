## What’s the difference between errors and exceptions
Errors cannot be handled, while Python exceptions can be handled at the run time. An error can be asyntax(parsing) error, while there can be many types of exceptions that could occur during the execution and are not unconditionally inoperable. An Error might indicate critical problems that a reasonable application should not try to catch, while an Exception might indicate conditions that an application should try to catch.

## What are exceptions and how to use them
The try and except block in Python is used to catch and handle exceptions. Python executes code following the try statement as a “normal” part of the program. The code that follows the except statement is the program’s response to any exceptions in the preceding try clause.
![](https://files.realpython.com/media/try_except.c94eabed2c59.png)

## How to correctly handle an exception
A try clause can have any number of except clauses to handle different exceptions, however, only one will be executed in case an exception occurs.
We can use a tuple of values to specify multiple exceptions in an except clause. Here is an example pseudo code.
```
try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass
```
## What’s the purpose of catching exceptions
Exception handling makes your code more robust and helps prevent potential failures that would cause your program to stop in an uncontrolled manner. Imagine if you have written a code which is deployed in production and still, it terminates due to an exception, your client would not appreciate that, so it's better to handle the particular exception beforehand and avoid the chaos.
___
### Built-in Exceptions
``` bash
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StandardError
      |    +-- BufferError
      |    +-- ArithmeticError
      |    |    +-- FloatingPointError
      |    |    +-- OverflowError
      |    |    +-- ZeroDivisionError
      |    +-- AssertionError
      |    +-- AttributeError
      |    +-- EnvironmentError
      |    |    +-- IOError
      |    |    +-- OSError
      |    |         +-- WindowsError (Windows)
      |    |         +-- VMSError (VMS)
      |    +-- EOFError
      |    +-- ImportError
      |    +-- LookupError
      |    |    +-- IndexError
      |    |    +-- KeyError
      |    +-- MemoryError
      |    +-- NameError
      |    |    +-- UnboundLocalError
      |    +-- ReferenceError
      |    +-- RuntimeError
      |    |    +-- NotImplementedError
      |    +-- SyntaxError
      |    |    +-- IndentationError
      |    |         +-- TabError
      |    +-- SystemError
      |    +-- TypeError
      |    +-- ValueError
      |         +-- UnicodeError
      |              +-- UnicodeDecodeError
      |              +-- UnicodeEncodeError
      |              +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
```