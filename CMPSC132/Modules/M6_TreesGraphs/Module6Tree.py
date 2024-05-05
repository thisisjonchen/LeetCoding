'''
### Trees
Consists of nodes and its connections are called edges
    Root of the tree is on top
    The bottom nodes are also named leaf nodes or external nodes
    A node cannot be reachable by itself other than the root

Tree Vocab:
    Edge: line between two nodes
    Path: the edges FROM root to specfied node (not from child to parent)
    Height: Number of edges from specified node to root (NOTE: Starts from Child and Specified Node)
    Height of Tree: Number of edges from lowest node (Leaf) to root (longest path)
    Depth: Number of edges from node to root (NOTE: Do not care about path and direction)

    Height vs. Depth: Height typically refers to the height of the entire tree, while depth is from specified node to root

    Level: Root is Level 1, Next is Level 2, etc.

Tree Properties:
    ONE Node of the tree is designated as the root node
    Every node n, except the root node, is connected by an edge from one to another where p is the parent of n
    A unique path traverses from the root to each node
    > Binary Tree: if each node in the tree has a MAXIMUM of two children, we say that the tree is a binary tree

# Binary Tree
A DS where every node has a max of two children. Typically name left and right children.

Types of Binary Trees:
    Full Binary Tree: Each node is a leaf or possesses EXACTLY two children, branches DONT have leaves on the same level
    Complete Binary Tree: The parent nodes of leaf has one missing node (filled from left to right)
    Perfect Binary Tree: Each parent has two child nodes (leaves) on the SAME level (compared to Full)
    Degenerate Binary Tree: Basically a Linked List (one branch, one child, one leaf)

Binary Tree Propoerties:
    A binary tree with k levels has NO MORE than 2^(k-1) nodes as leaves
        So say we have 2 levels, we can only have 2 nodes; 3 levels, 4 nodes

With the implementation of Nodes, we have a left and right pointer:
    class Node:
        def __init__(self,value):
            self.value = value
            self.left = None
            self.right = None

## Binary Search Tree (BST):
    Formula: LeftNode <= Node <= RightNode
    First Value will be the Root

## Traversals: Visits all Nodes
    # Breadth-First Search (BFS): Traverses the tree in level order, will vist every node on a level BEFORE going to a lower level
    # Depth-First Search (DFS): Go as DEEP as possible down one path before backing up and trying a different one
        There are three commonly used versions:
            Preorder Traversal: Root-Left-Right
            Inorder Traversal: Left-Root-Right
            Postorder Traversal: Left-Right-Root
    
    Which traversal should we use? 
        Preorder: Explore roots before inspecting any leaves (possibly for creating a replica of the tree)
        Inorder: Flatten tree into its original sequence (in non-decreasing order)
        Postorder: Explore leaves before any nodes (possibly for deleting a tree from leaf to root)

## Binary Heap
    Heap Strucutre: A binary heap is a COMPLETE binary tree
    Heap Ordering:
        Min-Heap: Every child GREATER THAN OR EQUAL TO parent (increasing toward leaves), min at root
        Max-Heap: Every child LESS THAN OR EQUAL TO parent (decreasing toward leaves), max at root

    Implementation: as these are complete trees, they are often stored as arrays of entries and ordered by BFS with the root at index 1
    NOTE: FILLS FROM LEFT TO RIGHT from LEVEL TO LEVEL, NOT SORTED.

    Compared to Binary Tree:
        Binary Heap is sorted via path, Binary Tree is sorted via option.
        Biggest giveaway is if root is min (POSSIBLE heap, check more) OR left is smaller than parent and right is bigger than parent (tree)

    Some Operations:
        To find min: return array[1] or top of heap
        To delete min (percolate down):
            1. remove root
            2. move the RIGHTMOST leaf node at root (array[last])
            3. Find the smallest child of the node
            4. swap node with its smallest child if needed
            5. repeat (3) and (4) until no swaps are needed (recursion)
        To insert (percolate up):
            1. Add element to bottom level
            2. Compare added element with its parent; if they are in the correct order, stop
            3. If not, swap the element with its parent and return to the previous step
            4. repeat (2) and (3) until no swaps are needed (recursion)

## Balanced Trees
    Require a Balance Condition so when we build the BST, we can ensure it is balanced (run in logn, not n time)
        Balanced trees have levels that are the same or nearly equal to one another.

    For self-adjusting, a BT operation is needed: Rotation
        Change the relative height of left and right subtrees WHILE preserving the binary search tree by rotating (algo: AVL)

## AVL Trees
    A self-balancing BST

    Structural props:
        Binary tree prop and order prop: same as BST
        Balance condition: balance of every node is between -1 and 1
            where balance(node) = height (node's left subtree) - height(node's right subtree)
            Compare all subtrees to check for balance -1 <= balance <= 1
 
    4 Cases of Unbalanced Trees:
        #1: L-L: parent balance is 2, left child balance is 1, rotate right around parent
        #2: R-R: parent balance is -2, right child balance is -1, rotate left around parent
        (For below, make line by pulling bottom into middle)
        #3: L-R: parent balance is 2, left child balance iis -1, rotate around child, rotate right around parent
        #4: R-L: parent balance is -2, right child balance 1, rotate right around child then rotate left around parent

    Advantages:
        All operations are log in the worst-case because trees are always balanced
        Has capabilities of self-balancing
    Disadvantages:
        AVL trees are difficult to implement
        Asymptotically faster but rebalancing costs time
        More space for heigh field
'''
