#LC 438. Find All Anagrams in a String
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p) # O(plogp)
        output = []
        for i in range(len(p),len(s)+1): #O(s)
            if sorted(s[i-len(p):i]) == p: # O(plogp)
                output.append(i-len(p))
        # Utlimately O(s*plogp)...not the most effective solution.
        return output

'''
TLDR: Utilize sliding window, then compare the sorted window to a sorted p (not recommended).

What could be better: Time complexity, could utilize a solution to improve it by iterating through p without sorting the window.
'''
