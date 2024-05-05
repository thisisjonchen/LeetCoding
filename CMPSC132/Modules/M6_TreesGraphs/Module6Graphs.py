'''
### Graphs
    A data strcuture with nodes (vertices) that are connected by edges
    Can be "directed" (can only move one way) or "undirected" (can move any direction)
    Edges can represent distance or weight
    Can also contain cycles (cyclic vs. acyclic)

# Key Terms
    Vertex (Nodes): a fundamental part of a graph, contians name and additional info
    Edge: Connects two vertices to show that there is a relationship between them. Can be oneway or two way
    Weight: Pertains to edges, may be weighted to show that there is a cost to go from one vertext o another
    Path: sequence of vertices that are connected by edges
    Cycle: Path that starts and ends at the same vertex (Cyclic). Without is acyclic. A directed graph with NO CYCLES is called a directed acyclic graph (DAG)

    Can be represented by G=(V,E) where V is a set of vertices and E is a set of edges. Each edge is a tuple.

# Edges
    Tree Edges: Edges we encounter while down one path of a graph
    Non-Tree Edge:
        Forward Edge: Allows us to move "forward through the graph, and potentailly be part of another path down the tree
        Backward Edge: Connects a node in a grh "back up" to one of its ancestors
        Cross Edge: Connects to sibling nodes that don't necessarily share an ancestor down in a tree path, but connects them anyways

        If there is a backward edge, there is a cycle in the the graph

# Graph Representation
    Adjacency Matrix: When two vertices are connected by an edge, we say that they are adjacent (we represent this via nested lists with weighting; empty spaces are with 0)
    Adjacency List: For more sparse lists, we can represent them via dictionaries, where each node contians a list of their respective adjacents

# Graph Traversal
    BFS: Starts at some arbitrary node in the graph and explores all of the neighbor nodes ath the present depth before moving on to the nodes at the next depth level
    DFS: Starts at some arbitrary node in a grpah and explores as far as possible long each branch before backtracking
        Go down the path until you hit a dead end 

# Topological Sorting  
    Takes a DAG and produces a linear ordering of all its vertices such that if the graph contains an edge (v, w) then the v comes before w in ordering
    Any linear ordering in which all the arrows go RIGHT is a valid solution
    Topological sorting for a graph is no possible if the graph is not a DAG

    * Use DFS here

    Step 1: Perform DFS for Graph
    Step 2: Store the vertices in a list in decreasing order of FINISH time
    
# Cycle Detection using DFS
    Once we backtrack and find a same node TWICE, it means there is a cycle

# Shortest Path in a Graph
    What is the shortest path between node A and E in the following weighted, undirected graph?

    ## Use Dijkstra's Algo
        Used to determine the shortest path from one node (or vertext) in a graph to every other node within the same graph data structure.
        The algorithm will run until all nodes in the graph have been visitied, thus, the shortest path betwen any 2 nodes can be saved and looked up after.
        
        Four Steps:
            1. From the starting node, visit the node with the smallest known distance
            2. Once you have moved to the smallest-distance node. Check each of its neighboring nodes
            3. For each neighboring node, compute the distance for the neighboring nodes by summing the distance of the edges leading from the start node
            4. If the distance to a node is less than a known distance, update the shortest distance for that node


## Hash Table
    Collection of items which are stored in such a way as to make it easy to find them later.
    Each position of te hash table, often called a bucket, can hold an item and ist named by an integer value starting at 0

    # Hash Function
        The mapping between an item and the bucket where that item belongs in the hash table is called the hash function
        A good hash function must be efficiently computable and should uniformly distribute the keys
        The modular method is the most common hash function: it simply takes an item and mod it by the table size, returning the remainder as its hash value.

        A hash function that maps each item into a unique bucket is referred to as a perfect hash function, BUT
        unfortunately, given an arbitrary collection of items, there is no systematic way to construct a perfect hash function.
        
        The GOAL: to create a hash function that MINIMIZES the number of collisions, is easy to compute, and evenly distributes the items in the hash table.

        # Folding Method
            Divide the item into equal-size pieces (the last piece may not be of equal size)
            Add the pieces to obtain the item to be hashed
                Some folding methods go one step further and reverse every other piece before the addition

        # Mid-square Method
            Square the item
            Extract some portion of the resulting digits
        
        # Hashing a string
            Convert each character of the string into ordinal values
            Add the ordinal values and use the modular method to get a hash value using ord(c)

    # Modular Hashing
        Once the hash values have been computed, we can insert each item into the hash table at thte designated position.
        The load factor (lambda) of a hash table is commonly denoted by lambda = (# of items) / (table size)
        
    # Collision
        When we want to search for an item, we simply use the has function to compute the bucket name for the item and then check the hash table to see if it is present
        This technique is going to work only if each item maps to a uniqiue location in the hash table
        
        -> Collision is when two or more items need to be in the smae bucket, and it creates probelms for the hashing technique

    # Collision Resolution (Rehashing)
        When two items hash to the same bucket, we must have a systematic method for placing the second item in the hash table

        # Open Addressing
            Try to find the next open bucket in the hash table
            In general: hash_index = (hash_index + skip) % hash_table_size

            If that doesn't work, we use Linear Probing:
                Visiting each bucket one at a time is an open addressing technique
                Start at the original hash value position and then move in sequential manner through the buckets UNTIL we encounter the first bucket that is empty.
        
    
## Minimum Spanning Trees
    Aspires to minimize the total length of wire connecting the computers

    # Spanning Tree
        A subgraph that contains all the vertices and is a tree.
        A graph may have many spanning trees.

    For a given graph, a MST is the spanning tree of MINIMUM cost for that graph. A MST is not necessarily unique.
    The goal is to visit all nodes at a minimum cost.

    # Prim's Algo
        Choose a random vertex from the graph as root node
        Add the edges that are connected to v into some data strucutre
        Find the edge in D with the minimum weight, that DOESN'T form a cycle, and add it to the MST
        Repeat step 2
    
    # Kruskal's Algo
        Sort the graph edges in their increasing order of weight
        Start adding edges to the MST from the edge with the smallest weight until the edge of the latgest weight
        Only add edges that DON'T form a cycle.
    
        

'''