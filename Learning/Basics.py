# Everything I Should Know in Python (I am primarily a Java Dev)
# Notes taken from NeetCode: https://youtu.be/0K_eZGS5NsU?si=FDNErxfgSBTaxCG9

### Basics
# Variables are dynamically-typed (ex: n)
# n can be anything (int, String, bool, etc. without declaring them)
n = 0 # Integer
n = "abc" # String
n = False # Boolean

# You can also have multiple assignments consisting of various types
n, m, z = 0, "abc", False

# Increments
n = n+1 # Good
n += 1 # Good
#n++ # Bad, exists in Statically Typed, but since Python is Dyn, can't do it here.

# None is null (absence of variable)
n = None

# Indentation (no need for parentheses or braces)
n=1
if n > 2:
    n-=1
elif n == 2:
    n +=2
else:
    n +=4

# However, parentheses are needed for multi-line conditionals
n, m = 1, 2
if ((n > 2 and 
    n!=m) or n==m):
    n+=1

# While Loop (ex: count to 0-4)
n = 0
while n < 5:
    print(n)
    n+=1

# For Loop (ex: count to 2,5)
for i in range(2,6):
    print(i)

# For Loop (ex: counting down from 5 to 2)
for i in range(5, 1, -1):
    print(i)

# Division is decimal by default
print(5/2) #2.5
print(5//2) # Floor, 2
print (-3//2) # -2, Most languages are -1 (rounds down always)
print(int(-3/2)) # -1, -3/2 = -1.5, int rounds up

# Modding is similar to Java
print(10 % 3) # 1
print(-10 % 3) # 2 for some reason, supposed to be -1

# We have to use 'import math' to use math.fmod to be consistent with Java
import math
print(math.fmod(-10,3)) # -1

# Some more math funcs
print(math.floor(3/2)) # round down
print(math.ceil(3/2)) # round up
print(math.sqrt(2)) # sqrt
print(math.pow(2,3)) #2^3 = 8

# Python numbers are infinite so they never overflow
float("inf") # can check if num is less than inf
float("-inf") # can check if num is less than -inf

### Data Structures
## Arrays (lists in python)
arr = [1,2,3]

# Can be used as a stack with .append or .pop
arr.append(4) # [1,2,3,4]
arr.append(5) # [1,2,3,4,5]

arr.pop() # removes last index value => [1,2,3,4,5] > [1,2,3,4]

# Can also insert (but o(n))
arr.insert(1,7)
# Using arr[i] would be faster (o(1))

# Initialize arr of size n with default val of 1
n = 5
arr = [1] * n # [1,1,1,1,1]

# CAREFUL: -1 is NOT out of bounds
# it's the last value, -2 is second to last, -3 is third to last, etc.
arr = [1,2,3]
print(arr[-1]) # 1
print(arr[-2]) # 2

# Sublists (aka slicing)
arr = [1,2,3,4]
print(arr[1:3]) # [2,3], includes first, excludes last
print(arr[0:4]) # [1,2,3,4]

# Unpacking
a, b, c = [1,2,3] # Assigns variables on left hand to respective arr index value

# Looping through arrays
nums = [1,2,3]

# Using Index
for i in range(len(nums)):
    print(nums[i])

# Without Index
for n in nums:
    print(n)

# With Index AND Value
for i, n in enumerate(nums):
    print(i, n)

# Loop through multiple arrays simultaneously with unpacking
nums1 = [1,3,5]
nums2 = [2,4,6]

for n1, n2 in zip(nums1,nums2):
    print(n1,n2)

# Reverse
nums = [1,2,3]
nums.reverse()
print(nums) # 3, 2, 1

# Sorting
arr = [5,4,7,3,8]
arr.sort()
print(arr) # 3,4,5,7,8

arr.sort(reverse=True) # Reverses order > 8,7,5,4,3

# Sorting Strings
arr = ["bob", "alice", "jane", "doe"]
arr.sort() # sorts alphabetically
print(arr) # ["alice", "bob", "doe", "jane"]

# Custom sort (ex: by length of string) using key=lambda
arr.sort(key=lambda x: len(x))

# List comprehension
arr = [i for i in range(5)] # [0,1,2,3,4]
arr = [i+i for i in range(5)] # [0, 2, 4, 6, 8]

# 2-D Lists/Arrays
arr = [[0] * 4 for i in range(4)] # creates 4x4 list of [0]

# This won't work
arr = [[0]*4] * 4 # still creates 4x4 list of [0], but each row is the same if inner is changed

## Strings
# Strings are similar to arrays
s = "abc"
print(s[0:2]) # Slicing, "ab"

# Strings are immutable
# Adding to a string will create a new string (o(n))
s += "def" # new s "abcdef"

# Valid numeric strings can be converted to Int
print(int("123") + int("123")) # 246

# And numbers can be convert to strings
print(str(123) + str(123)) # 123123

# If ASCII value is needed (rare cases)
print(ord("a")) # 97
print(ord("b")) # 98

# Combine a list of strings with a delimitor
strings = ["ab", "cd", "ef"]
print("".join(strings)) # abcdef
print(" ".join(strings)) # ab cd ef

## Queues
from collections import deque
queue = deque() ## creates a queue
queue.append(1)
queue.append(2)
print(queue) # deque([1,2])

queue.popleft(1) # unlike stacks, we can pop from the left (FIFO rather than FILO) and in constant time
queue.pop() # we can also make it act like a stack
queue.appendleft(1) # we can also append to the beginning as well
print(queue)

## HashSets
# Good for identifying duplis (can't have any duplis), we can search in constant time
mySet = set()
mySet.add(1)
print(1 in mySet) # true

# Initialize sets
mySet = set([1,2,3]) # can use list

# Can also use set comprehension (like list comprehension)
mySet = {i for i in range(5)}

## HashMaps (aka dict, key-pairs)
myMap = {}
myMap["alice"] = 88
print(myMap) # {"alice": 88}

# Can search using key and return value in constant time
print("alice" in myMap) # 88

# Initialize maps
myMap = {"alice": 90, "bob": 70} # key left : value right

# Can also use map/dict comprehension
myMap = {i : 2*i for i in range(3)} # has colon to diff key and value

# Looping through maps
myMap = {"alice": 90, "bob": 70}
for key in myMap:
    print(key, myMap[key]) # prints key value

for val in myMap.values():
    print(val) # prints all vals

for key, val in myMap.items():
    print(key, val) # prints key value too

## Tuples
# Like arrays but IMMUTABLE (like standard arrays in Java vs. ArrayLists)
tup = (1,2,3)

# Can be used as key for hash map/set
myMap = {(1,2) : 3} # tuple key
mySet.add((1,2)) # tuple pair in set

# This is useful as lists can't be keys
myMap[[3,4]] = 5 # doesnt work

## Heaps
# Python uses minHeaps by default, with arrays under the hood
import heapq
minHeap = []
heapq.heappush(minHeap, 3) # 3
heapq.heappush(minHeap, 2) # 2,3
heapq.heappush(minHeap,4) # 2,3,4

# Min is always at index 0
print(minHeap[0]) # 2

while len(minHeap):
    print(heapq.heappop(minHeap)) # prints smallest to largest 2,3,4

# Can reverse (or have maxHeap) by * by -1 on push and -1 on pop to negate org. -1
maxHeap = []

heapq.heappush(maxHeap, -3) # 3
heapq.heappush(maxHeap, -2) # 2,3
heapq.heappush(maxHeap, -4) # 2,3,4

while len(minHeap):
    print(-1 * heapq.heappop(maxHeap)) # prints largest to smallest 4,3,2

# Build heaps from initial array in linear time
arr = [2,1,8,4,5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr)) # prints out "sorted" 1,2,4,5,8 smallest to largest

## Functions
def myFunct(n,m): # quite simple
    return n*m

# Nested functions have access to outer variables
def outer(a,b):
    c = "c"

    def inner():
        return a + b + c
    return inner()

print(outer("a","b")) # abc

# Can modify objects but not reassign UNLESS using nonlcoal keyword
# ex: if myFunc(arr, val), can't redeclare val unless nonlocal val
def double(arr,val):
    def helper():
        # Modifiying array works
        for i in range(arr):
            arr[i] *= 2
        
        nonlocal val
        val *= 2
    
nums = [1,2]
val = 3
double(nums, val) # [2,4] 6 < 6 from inside of double, not passed

## Class
# "self" is kind of like "this" in Java
class MyClass:
    # Constructor
    def __init__(self, nums):
            # create member variables
            self.nums = nums
            self.size = len(nums)
    
    # self key word req as param
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength
    
# That is all with the basics! Now back to work :)