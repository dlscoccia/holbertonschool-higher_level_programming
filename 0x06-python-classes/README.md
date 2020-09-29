# 0x06. Python - Classes and Objects :snake:
![](https://media.geeksforgeeks.org/wp-content/uploads/20191013164254/encapsulation-in-python.png)
## What is OOP
Object-oriented programming is a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields, and code, in the form of procedures. A feature of objects is that an object's own procedures can access and often modify the data fields of itself.
## “first-class everything”
The creator of Python Guido Van Rossum designed the language in accordance with that principle. What it essentially means that all the functions, classes, modules, methods and data types all have equal status.
“Everything is treated the same way.”

## What is a class
Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

Python classes provide all the standard features of Object Oriented Programming: the class inheritance mechanism allows multiple base classes, a derived class can override any methods of its base class or classes, and a method can call the method of a base class with the same name. Objects can contain arbitrary amounts and kinds of data. As is true for modules, classes partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation.

Python Classes
A class is a Python object with several characteristics:

You can call a class object as if it were a function. The call, often known as instantiation, returns an object known as an instance of the class; the class is known as the type of the instance.

A class has arbitrarily named attributes that you can bind and reference.

The values of class attributes can be descriptors (including functions), covered in “Descriptors”, or normal data objects.

Class attributes bound to functions are also known as methods of the class.

A method can have a special Python-defined name with two leading and two trailing underscores (commonly known as dunder names, short for “double-underscore names”—the name __init__, for example, is often pronounced as “dunder init”). Python implicitly calls such special methods, if a class supplies them, when various kinds of operations take place on instances of that class.

A class can inherit from other classes, meaning it delegates to other class objects the lookup of attributes that are not found in the class itself.
## What is an object and an instance
An object is simply a collection of data (variables) and methods (functions) that act on those data. Similarly, a class is a blueprint for that object. We can create many objects from a class. An object is also called an instance of a class and the process of creating this object is called instantiation.
An object has two characteristics:
    • attributes
    • behavior

## What is the difference between a class and an object or instance
An object (instance) is an instantiation of a class. When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.
## What is an attribute
Class attributes are variables of a class that are shared between all of its instances. They differ from instance attributes in that instance attributes are owned by one specific instance of the class only, and ​are not shared between instances.
![](
## What are and how to use public, protected and private attributes
Protected members are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.

Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any base class. In Python, there is no existence of Private instance variables that cannot be accessed except inside a class. However, to define a private member prefix the member name with double underscore “__”.
## What is self
The self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in python. It binds the attributes with the given arguments
## What is a method
Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.
## What is the special __init__ method and how to use it
Class functions that begin with double underscore __ are called special functions as they have special meaning.
Of one particular interest is the __init__() function. This special function gets called whenever a new object of that class is instantiated and is one of the reserved methods in Python. 

In object oriented programming, it is known as a constructor. 

The __init__ method can be called when an object is created from the class, and access is required to initialize the attributes of the class.

## What is Data Abstraction, Data Encapsulation, and Information Hiding
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variable. 

## What is a property
A property, in some object-oriented programming languages, is a special sort of class member, intermediate in functionality between a field (or data member) and a method.

## What is the difference between an attribute and a property in Python
Properties are special kind of attributes which have getter, setter and delete methods like __get__, __set__ and __delete__ methods.

## What is the Pythonic way to write getters and setters in Python
there is a property decorator in Python which provides getter/setter access to an attribute Properties are a special kind of attributes.

In Python, you can define getters, setters, and delete methods with the property function. If you just want the read property, there is also a @property decorator you can add above your method.
```
class C(object):
    def __init__(self):
        self._x = None
#C._x is an attribute
@property
    def x(self):
        """I'm the 'x' property."""
        return self._x
# C._x is a property   This is the getter method
@x.setter # This is the setter method
    def x(self, value):
        self._x = value
@x.deleter # This is the delete method
    def x(self):
        del self._x
```
## What is the __dict__ of a class and/or instance of a class and what does it contain
This is the dictionary containing the module’s symbol table.

#### Getting an attribute from a class
When you use the syntax C.name to refer to an attribute on a class object C, the lookup proceeds in two steps:
```
When 'name' is a key in C.__dict__, C.name fetches the value v from C.__dict__['name']. Then, when v is a descriptor (i.e., type(v) supplies a method named __get__), the value of C.name is the result of calling type(v).__get__(v, None, C). When v is not a descriptor, the value of C.name is v.

When 'name' is not a key in C.__dict__, C.name delegates the lookup to C’s base classes, meaning it loops on C’s ancestor classes and tries the name lookup on each (in method resolution order, as covered in “Method resolution order”).
```
#### Getting an attribute from an instance
When you use the syntax x.name to refer to an attribute of instance x of class C, the lookup proceeds in three steps:
```
When 'name' is found in C (or in one of C’s ancestor classes) as the name of an overriding descriptor v (i.e., type(v) supplies methods __get__ and __set__)

The value of x.name is the result of type(v).__get__(v, x, C)

Otherwise, when 'name' is a key in x.__dict__

x.name fetches and returns the value at x.__dict__['name']

Otherwise, x.name delegates the lookup to x’s class (according to the same two-step lookup used for C.name, as just detailed)

When a descriptor v is found, the overall result of the attribute lookup is, again, type(v).__get__(v, x, C)

When a nondescriptor value v is found, the overall result of the attribute lookup is just v

When these lookup steps do not find an attribute, Python raises an AttributeError exception. However, for lookups of x.name, when C defines or inherits the special method __getattr__, Python calls C.__getattr__(x,'name') rather than raising the exception. It’s then up to __getattr__ to either return a suitable value or raise the appropriate exception, normally AttributeError.
```
___