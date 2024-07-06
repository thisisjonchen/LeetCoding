'''
### PART 1
# Object Oriented Programming
Combines data and functionality, wraps it inside an object. Everything in Python is an object, even traditional primitive types

In OOP:
    Each object has its own LOCAL STATE
    Use method calls to call its state
    Several objects may beinstances of a common type (inheritance)
    Different types may relate to each other 

Basic OOP Principles:
    Classes
    Data Abstraction (Deal with important details)
    Encapsulation (Hide unnecessary details inside a class)
    Inheritance (Reuse functionality)
    Polymorphism (Define more than one function with the same name)

Class is the blueprint. Objects are instances of the class.

# A class looks like this (uppercase class name):

class ClassName:
    <body>

ex:
class Dog:
    number_of_legs = 0
    
    def eat():
        return "I am eating..."

In Python, variables in classes are called attributes.

When calling a class:
    A new instance of that class is created
    # The __init__ method of the class is called:
    ex:
    class Account:
        def __init__(self, name):
            self.holder=name
            self.balance=0
    
    SPECIFY instance attributes inside __init__() after "self"...this is basically the constructor

If you have a method that takes no arguments, then you still have to have one argument, the SELF.

Every object that is an instance of a user-defined class has a unique identity. Assigning another variable to a class aleady assigned just creates a reference to that.

hasattri() can check if a class has a specific attribute

Class attributes (declared outside of init, inside of class), are static and shared among all instances of the class

Special methods have double __ like __init__:
    __str__(self) -> can return object with custom string (like when printing)
    __repr__(self) -> does same as above... "represent"
    Operators for adding objects together
    __add__(self, other)
    __sub__(self, other)
    etc.

Use @property if you want to use a method like an ATTRIBUTE (no parentheses when called)

# Class Design
UML (Unified Modeling Language) Diagram: standard diagrams
    General Layout: Box divided into three sections
        Top: name of the class
        Middle: list of data attribute
        BottomL list of class methods

Technique for identifying classes:
    1. Get written description of the problem domain
    2. Identify all nouns in the description, each of which is a potential class
    3. Refine the list to include only classes that are relevant to the problem

    
### PART 2
# Inheritance
Classes can extend the definition of other classes
    Allows the use of methods and attributes already defined in the previous one (superclass)
    However, seperate subclasses can not use eachother's methods (only superclass)

To define a subclass, put the name of the super class in () after the suclass name on the first line of the definition:

class <name>(<parent class>):
    <body>

ex:
class Dog(Animal):
    <body>

We also use super().<method>, like __init__

def Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # NO NEED TO SET EQUAL TO A VARIABLE (like self.name)

issubclass(<subclass>,  <parent>) is also helpful to check if a class is a subclass of another.

# Polymorphism (many forms)
Is when subclasses make use of BASE CLASS methods or overriding them (like speak(), different animals may have a different speak() function)
Can support:
    Method Overriding
    Operator Overloading
    Method Overloading

# Object Construction
The __new__ method may be useful in customizing instnace creation (like checking if inputs are valid before creating)

# Method Inputs
In Java, we can specify methods with a specified number of inputs ex: speak(x, y, z) ; speak(x, y) speak(x)
In Python, WE CANNOT DO THIS. If this is done, only the last defined method will be used.

To simulate this in Python, we have default vales ex: speak(x="woof")
This is such that if no input is inputted, it will default to it.

# Abstraction 
Abstraction is the process of simplifying complex processes into a simpler process that can be re-used.

Abstract classes are classes that contain one or more abstract methods
    Abstract methods: a method that is declared, but contains NO IMPLEMENTATION (like an interface)

Abstract classes may NOT be instantiated, and require subclasses to provide implementations for the abstract methods.

The ABC import: from abc import *
@abstractmethod annontation
ex:
    class Vehicle(ABC): <<< abstract class
        @abstractmethod
        def drive(self):
            raise NotImplementedError("Subclass must implement abstract method") <<< requires subclass to implement said method

Some notes about abstract classes in Python...
    Abstract classes can have concrete AND abstract methods
    Abstract classes work as template for other classes
    If not implemented by subclass, Python throws error

    
# Encapsulation
Allows programmer to group data...
Concerns visibility (private, public)
    Everything in Python is public by DEFAULT
    
Public, Private, Protected:
    Public: add nothing... default: "dog"
    Protected: add single underscore: "_dog"
    Private: add double underscore: "__dog"

# ABSTRATION VS. ENCAPSULATION
Abstraction solves issues at the DESIGN level. Encapsulation solves it at the IMPLEMETATION level.
Abstraction hides unwanted details while showing essentials. Encapsulation wants all in one.
Abstraction allows focusing on what the info object must contain. Encapsulation means hiding the internal details or mechanics of an object.
'''