'''
### Data Structures
Def: an implementation of an abstract data type that requries a physical view
of the data using some collection of programming contructs.

A DS is a way of organizing and storing data so it can be modified EFFICIENTLY.

Linear Structures
    Stacks, queues, and linked lists are examples of data collections whose items are ordered depneding on how they are added or removed.
    They can have to ends (left or right, head or tail, top or bottom)
    What distinguishes them is how items are added or removed and what order they occur
        Variations appear in many algos and cna be used to solve a variety of problems.

# Linked List
Linked lists provide an alternative to an array-based sequence (like List).

Pros:
    Can live anywhere in memory (has pointers)
    As long as references are updated, each linked list node can be flexibly moved. (Better at moving than regular lists)
Cons:
    Have linear look up time. Starts at the beginning of the chain and moves down. (Worse at searching, esp at specific index, than lists)

Singly Linked List nodes contain a value and a "pointer" to the next node. Doubly Linked List nodes contain a value and two pointers, one to previous other to next. Allows for traversal both ways, but at the cost of more memory.
class Node:
    def __init(self, value):
        self.value = value
        self.next = None

LinkedList class (has attribute that points to the head value):
class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self):
        if self.head is None:
            return("The list is empty")
        self.head = self.head.next

# Inserting nodes:
A node can be added to a singly linked list in three ways:
    - At the front of the linked list
    - At the end of the linked list
    - After a given node

We have to traverse the list first to reach our specified node (linear search time), rather than inserting like lists.

# Doubly Linked List
Exactly like a singly linked list, but with a extra pointer that points to the previous node.

Pros:
    Can be traversed in both forward and backward direction
    Is more efficient if the pointer to the node to be deleted is given

Cons:
    Requires extra memory

# Circular Linked List
    A linked list where all node are connected to form a circle (last node point to first node, there is no NULL/NONE at the end)

Advantages:
    Any node can be a starting point
    Useful for implementation of queues
    Useful in applications to repeatedly go around the list.

## Stacks (LIFO)
    Ordered collection of items where the addition of new items and removal always takes place at the same end (like a pancake)

    Basic operations:
        Push: add
        Pop: remove
        isEmpty: check if stack is empty, else false
        Peek: Returns the top element without removing it
        Size: returns the number of items in the stack

    Implementation with "Nodes":
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    class Stack:
        def __init__(self):
            self.top = None
    
    def push(self, value):
        nn = Node(value)
        nn.next = self.top
        self.top = nn


## Queue (FIFO)
    Ordered colleciton of items where addition of new items start the end, removal at the head

    Basic operations:
        Enqueue: appends element to the tail of the queue
        Dequeue: remove an element from the head of the queue
        isEmpty: Returns True if queue is empty, else False
        Peek: Returns the element at the top of the queue without removing it
        Size: returns the number of items
    
    
    Implementation with "Nodes":
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    class Queue:
        def __init__(self):
            self.head = None
            self.tail = None

    def enqueue(self, value):
        nn = Node(value)
        self.tail.next = nn
        self.tail = nn

    ## Double Ended Queue (Deque)
        Insertions and deltions can occur at either end
        NOT heavily used.    
'''

'''
if postfix:
            postfix = postfix.split(" ")
            isPreviousExponent = False
            previousPower = 0
            i = 0
            for value in postfix:
                if self._isNumber(value):
                    calcStack.push(float(value))
                    if isPreviousExponent: # if two indexes over and no exponent is detected, it is not a exponential exponentiation
                        i -=1
                        if i == 0 : 
                            isPreviousExponent = False
                elif value == "^": # special exponent procedure if exponential exponentiation
                    power = calcStack.pop()
                    base = calcStack.pop()
                    if isPreviousExponent:
                        try: 
                            currentBase = base**(1/previousPower) # incase previous exponent was 0, the current should now be 1.
                        except ZeroDivisionError:
                            currentBase = 1
                        currentPower = previousPower ** power
                        calcStack.push(currentBase ** currentPower)
                        previousPower = currentPower
                    else:
                        calcStack.push(base ** power) 
                        isPreviousExponent = True
                        previousPower = power
                        i = 2
                elif value in "*/+-":
                    if isPreviousExponent:
                        previousPower = 0
                        isPreviousExponent = False
                    num1 = calcStack.pop()
                    num2 = calcStack.pop()
                    if value == "*": calcStack.push(num2 * num1)
                    elif value == "/":
                        try: 
                            calcStack.push(num2 / num1) # incase division by Zero
                        except ZeroDivisionError:
                            return None
                    elif value == "+": calcStack.push(num2 + num1)
                    elif value == "-": calcStack.push(num2 - num1)
            return calcStack.pop()
'''