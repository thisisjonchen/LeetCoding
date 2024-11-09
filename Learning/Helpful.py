from collections import defaultdict
# Some helpful functions

# sorted() 
# Time Complexity: O(n log n), where n is the length of string
# Auxiliary Space: O(1)
s = "ebcda"
s = sorted(s) # sorts a string or iterable object > abcde

# defaultdict(type)
# creates keys if it does not exist
map = defaultdict(int)
map = defaultdict(list)

# .values()
# returns values of an iterable in array, like hashmap
hashmap = {1: "a", 2: "b"}
hashmap.values() # returns [["a"], ["b"]]

# max(comp1, comp2), min(comp1, comp2)
# can be used to compare two values and determine the larger or smaller of the two. Returns whatever is smaller or larger.
max(1,2)
min(1,2)

# .lower(), .upper()
# converts all chars to lower or upper in a string
s = "booGie Woogie"
s.lower() # boogie woogie
s.upper() # BOOGIE WOOGIE 

# re.sub('[^0-9a-zA-Z]+', "", string)
# useful for replacing all alphanumeric numbers using regex (Two Pointers)
import re
s = "bruh ___EEEE**"
s = re.sub('[^0-9a-zA-Z]+', "", s)

# Heaps (Useful for creating Min-Heaps + Priority Queues)
import heapq
customers = []
heapq.heappush(customers, (2, "Bob")) # Notice how it is in (array, (priority, value))
# Can also use .heapify to create a priotity queue of a whole array of TUPLES
heapq.heapify(customers)
                           
