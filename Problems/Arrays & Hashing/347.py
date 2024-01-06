# LC 347. Top K Frequent Elements

from typing import List
from collections import defaultdict

# Initial Solution (Time O(n) + O(nlogn))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        hashmap = dict(sorted(hashmap.items(), key=lambda items: items[1], reverse=True)) # reverse to bring highest "count" to first index
        return list(hashmap.keys())[0:k]
    
# Better Solution (Time O(n+k) = O(n)) by NeetCode
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # create an array with index as the count (meaning, the index/count's max can only be as large as the nums array)
        for num in nums: # (1)
            count[num] = 1 + count.get(num, 0) # loop through nums and assign to count dict with index being nums, count being value
        for n, c in count.items(): # (2)
            freq[c].append(n) # this is where we kinda flip it to where the index is the count, nums being value (basically swapping "keys" and values)
        result = []
        for i in range(len(freq) -1, 0, -1): # looping through to add to an array, as req by List[int]
            for n in freq[i]:
                result.append(n)
            if len(result) == k:
                return result
        
'''
TLDR: Use hashmap with key being nums and value being the "counter". Use a result array with loop bounded by k to output respective values.

Explaination:
My initial solution uses a dict/hashmap to create key-pairs of the "number" : counter of "numbers". We iterate through
the nums array to build the dict (time O(n)) and sort it (time O(nlogn)). Then we return the list of keys from index 0 to k.
My worry here was the time (O(n) + O(nlogn) + memory complexity (O(n)) and if I could optimize this further.

NeetCode describes how he used multiple arrays to achieve the same effect, albeit in O(n) time. This was done by using
a count list and freq array to keep track of the count of numbers using the index of the freq array and storing the respective numbers
as the value. At the end, he used a for loop to iterate through to add k values (starting from the last index of freq) to a result array
then outputting that once it (the length of result) reaches k.

I was a bit confused on how this solution was O(n), but a commenter on his YT video stated how firstly, the loop through nums (1) is O(n),
then the operation after is also O(n), (2). Therefore, the time complexity is still O(n). The last result loop to append the numbers is O(k),
where k is the number specified by the user, which is max size "n" or smaller. As k is equal or smaller, this is makes it O(n+k), which equals O(n).

Fascinating!
'''