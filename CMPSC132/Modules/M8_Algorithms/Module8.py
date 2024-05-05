'''
### Algorithms Introduction
    When considering a program, two main resources to consider are time and memory
    The resource to optimize depends on the application an the computing system.
    The amount of resources consumed often depnds on the amount of data you have.

    Algos care about the growth rate of resource consumption with respect to the the data size:
        Worst-Case: The max number of steps on any instance of size n.
        Best-Case: The min number of steps take in any instance of size n.
        Average Case: An average number of steps taken in any instance of size n.

    # Time Consumption
        Impementations of the same problem can require different amounts of time

    # Space Consumption
        Is another resource that gets consumed by programs as they execute
            Values and frames in active environments consume memory
            Memory used for other values and frames can be recycled

        # Active environments
            Environments for any function calls currently being evaluated
            Parent environemtns of functions named in active environments
    
    # Asymptotic Analysis
        The asymptotic behavior of a function f(n) refers tot he growth of f(n) as n gets large.
        We typically ignore SMALL values of n, since we are usually interested in estimating how slow the program will be on large inputs.
        
    ## Growth Rates
        A method for bounding the resources used by a function by the size of a problem, where:

        T(n) = O(f(n))

        Where thare are TWO positive constants k1 and k2 such that:

        k1 * f(n) <= T(n) <= k2 * f(n) for all n greater than some minimum m.

    # Big O Notation
        One of the formal notational methods for stating the growth of resource needs (efficiency and storage) of an algorithm and usually defines the Worst Case.

        Properties:
            Constants (like 2 * n) do NOT affect the growth of a process.
            Logarithms: THe base of a logarithm DOES NOT affect the order of growth of a process
            Nesting: When an inner process is repeated for each step in an outer process, multiply the steps
            in the outer and inner process to find the total numbers of steps.

        Orders of Growth:
            Exponential (2^n)
            Cubic (n^3)
            Quadratic (n^2)
            Log Linear (n log n)
            Linear (n)
            Logarithmic (log n)
            Constant (1)
            


'''