'''
### Functions
    Domain is the set of all inputs it might possibly take as arguments
    Range is the set of output values it might possibly return

    A pure function's behavior is the relationship it contains between the domain and range.

    Designing a function: 
        Give it exactly one job
        Don't repeat yourself.

    # Higher-Order Functions
        A function that takes ANOTHER function as an argument.

        Used to:
            Express general methods of computation.
            Remove reptition from programs.
            Seperate concerns among functions.
    
    Imperative vs. Functional:
        Imperative requires other variables declared locally
        Functional just uses its own inputs to return an output
    
    # Lambda Expressions
        Anonymous functions that are usually passed as parameters to other funcitons

        Syntax:
            lambda argument_list: expression
            lambda x, y : x + y

        Lambda expression can only have one line of code and automatically return the computed value, so they do not need the return statement.
    
        # Map()
            Takes a function and a collection of items, then makes a new empty collection, runs the function on each item in the og collection,
            then inserts each return value into the new collection. Returns the new collection.

            map(func, list)
        
        # Filter()
            Way to filter all elements for which a function returns true. It creates a new list with with all the elements the func returned true.

            filter(func, list)

        # Reduce()
            Applies a function on a list of elements to reduce the sequence into one value.

            reduce(func, list)
        
        # List comprehension
            A more concise way to create lists.

            list(map(func, range)) or [func for x in range]

    ## Iterators + Generators

        # Iterables
            Can be for-looped over, is an object that supports __iter_, returns iterator, or __getitem__ for indexed lookup.
            Can be represented without each element being stored explicitly in the memory
                Known as lazy evaluation/computing
            All iterators are iterables; not all iterables are iterators.
'''
