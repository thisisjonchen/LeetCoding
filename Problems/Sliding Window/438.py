#LC 438. Find All Anagrams in a String

# 5/19/24 - O(s*plogp)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p) # O(plogp)
        output = []
        for i in range(len(p),len(s)+1): #O(s)
            if sorted(s[i-len(p):i]) == p: # O(plogp)
                output.append(i-len(p))
        # Utlimately O(s*plogp)...not the most effective solution.
        return output
        
# Retry 7/16/24 - Massively Better O(n)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        l, r = 0, 0
        res = []

        pFreq = defaultdict(int)
        for char in p: 
            pFreq[char] += 1

        while r < len(p) - 1:
            if s[r] in pFreq:
                pFreq[s[r]] -= 1
            r += 1

        while r < len(s):
            if s[r] in pFreq:
                pFreq[s[r]] -= 1
            if all(value == 0 for value in pFreq.values()):
                res.append(l)
            r += 1
            if s[l] in pFreq:
                pFreq[s[l]] += 1
            l += 1

        return res

'''
Initial TLDR: Utilize sliding window, then compare the sorted window to a sorted p (not recommended).
What could be better: Time complexity, could utilize a solution to improve it by iterating through p without sorting the window.

Retry TLDR: Once again, utilize sliding window. However, now also use a hashmap over p (if all values from "p" are 0, then it is a anagram). We maintain the window size and slide by 1 each time.
'''
