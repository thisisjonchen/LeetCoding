'''
### Introduction to Sorting and Searching
    Searching typically answers true or false as to whether the item is present and some it may be modified to return where the item is found
    Sorting processes a collection of items and places them in some kind of order (can take a substantial amount of resources)

    The efficiency of searching and sorting algorithms is related to the number of items being processed.

# Searching
    Linear Search | O(n):
        Start from the leftmost element of the list and go to the right either until you find the item or you run out of items to compare.
        To find an item x with Linear search:
            Use a simple iterative approach
    
    Binary Search | O(logn):
        Takes a SORTED list and starts by examing the middle item. The ordered nature of the list allows us to elinate half of the items.
        To find an item x with Binary Search:
            Compare x with the middle element
            If x if greater, recur in the right half of the subarray. Smaller, recur in left.
    
    # Divide-and-Conquer paradigm
        A problem that we want to solve may be TOO BIG to understand or solve at once, so we divide the problem into smaller pieces, solve them, then reassemble.

        In Divide-and-Conquer, we break a problem down recursively, applying three steps at each level
            Divide: Break the given problem into subproblems of the same type
            Conquer: Recursively solve these subproblems
            Combine: Appropriately combine the answers
    
# Sorting
    Bubble Sort | Always O(n^2):
        Simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they  are in the wrong order
        Makes multiple passes through a list
        For swaps in python, you can just do:
            list[i], list[i+1] = list[i+1], list[i]

    Insertion Sort | Best: O(n) | Worst: O(n^2):
        The insertion sort algo is an inplace comparison that works by looking at the list as if it is being filled in
        Starts off in the first iteration as if it has only one element in it
        Numbers that come after are inserted in to the list at the correct position, sifting those items that are greater to the right.
    
    Quick Sort | Average: O(nlog(n)) | Worst: O(n^2):
        Divide-and-Conquer Algorithm that picks an element as pivot and partitions the given array around the picked pivot
        One side holds  elements smaller than the pivot and the other one holds elements that are greater than the pivot.
        The pivot can be totally random.
        There would be two pointers: right and left, where we increment the left and decrement the left until right <= left. If so, we exchange.
        Once right and left are on the same value, we swap the value with the pivot. Then we do a recur on the left and right.

    Merge Sort | Always: O(nlog(n))
        Another divide-and-conquer, commonly used.
        Continually spilts a list in half if the list is empty or has one item. Then, it merges and sorts as it goes to put the lists together.
        Is recursive.

    Selection Sort | Always: O(n^2)
        In-place comparison-based algorithm in which the listis divided into two parts, the sorted part at the left end and the unsorted part at the right end.
        Somewhat like bubble sort, but only makes one swap for every pass through the list.
        
    Heap Sort | Always: O(nlog(n))
        Uses the Binary Heap data structure.
        First find the maximum element and place the maximum element at the end. Same process for the remaining elements.
            Build a max heap from the unsorted list
            Since the largest item is stored at the root of the heap, replace it with the last item of the heap followed by reducing the size of the heap by 1.
            heapify the root of the tree.
            Repeat above steps while size of heap is greater than 1.
'''