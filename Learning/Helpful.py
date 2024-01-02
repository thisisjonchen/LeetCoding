from collections import defaultdict
# Some helpful functions

# sorted() 
# Time Complexity: O(n log n), where n is the length of string
# Auxiliary Space: O(1)
s = "ebcda"
s = sorted(s) # sorts a string or iterable object > abcde

# defaultdict(iterable)
# creates keys if it does not exist
map = defaultdict(list)

# .values()
# returns values of an iterable in array, like hashmap
hashmap = {1: "a", 2: "b"}
hashmap.values() # returns [["a"], ["b"]]

