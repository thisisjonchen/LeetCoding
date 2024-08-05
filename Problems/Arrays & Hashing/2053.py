# LC 2053. Kth Distinct String in an Array | LC Daily - 8/5/24
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = defaultdict(int) # Max O(26) SC
        for c in arr:
            freq[c] += 1
        
        for c in arr:
            if freq[c] == 1:
                k -= 1
                if k == 0:
                    return c
        return ""

'''
TLDR: Use hashmap + freq. If freq == 1, remove 1 from k until 0, of which we return the char.

TC O(n)
SC O(26) -> O(1) due to max unique chars in alphabet (lowercase) being 26.
'''

        
