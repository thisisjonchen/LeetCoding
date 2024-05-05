'''
# Errors:
    Syntax Errors: produced by Python when it is translating the source code into byte code
    Runtime Errors: produced by the runtime system if something goes wrong while the program is running
    Semantic errors: problems with a program that was translated into by code correctly and runs but does not do the right thing (not what the programmer intended)

Syntax Errors:
    Usually easy to fix and catch, details exact position
    Avoid keywords and remember colons and indentation
    Ex: SyntaxError: invalid syntax

Runtime Error:
    Program does absolutely nothing, infinitely hangs, or further exception (NameError, TypeError, KeyError, AttributeError (ex: has no function), IndexError)

Semantic Errors:
    Hardest to debug, programs runs fine, but does not do the right thing the programmer expected

# Debugging
Development Lifecycle: Requirements > Design > Coding > Debugging/Testing > Deployment > Requirements ...

Can be more time consuming to DEBUG than WRITE the code

Debugging Principles:
    Know what the code is doing
    Make it fail every time
    Change one thing at a time, for a reason, and keep track of what you have done
    Version control

Python debugger comes as part of Python as pdb
    You can trigger a debugging session by importing pdb and adding  pdb.set_trace() ABOVE the line where you would like the session to begin
    Useful pdb commands:
        next()
        step()
        up()

Writing testing code and running this code in parallel (unit testing) is a good practice > the unittest module (have to import)

Defensive Programming:
    Testing:
        Compare input + output: "How can I break my program?"
    Debugging:
        Analyze events leading up to an error: "Why is it not working?"

Try/Catch:
    In python, we use try and EXCEPT
    We can specify with exception by specifying it after except -> excpet ZeroDivisionError
    except by it self is a catch all

    Gives more control over if/else

# Memory
Python handles memory by mapping a name through a reference to an object through a private heap.
The user has no control over this memory (call frame (stack) and heap frame)

Call frames essentially store the functions and variables
Heap frames store the references to values
When functions in call frames update references, there is a new space allocated in heap frame and variables re-point to this reference

Garbage collection:
    Detects stale objects, deallocating space to those objects, and returning the reclaimed space to free the list
    Live objects are objects that have a direct or indirect refrence to that object

    Live objects with direct reference (a variable pointing to them) are called root objects
    An indirect reference to a live object may be inside a live array or field of some toher live object

    We can see an object's address through id(variable)
    if two variables have the same value, they point to the same reference (object address)
    sys.getrefcount(object) can return number of references

    Functions create new instances and stored seperate. When functions terminate, the space they used are freed.

Modeling Storage
    Global Space: Lasts until we quit Python
    Call Frame: Deleted when call is done
        Call Stacks: Functions are stacked, executes in order
    Heap Frame: Dynamically allocates space for objects (both functions and values with corresponding memory address)

    All objects are created in the heap frame and references are made in the call frame
'''