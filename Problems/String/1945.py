# LC 1945. Sum of Digits of String After Convert | LC Daily - 9/3/24
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def toSum(s):
            curr = 0
            for c in s:
                curr += int(c)
            return curr

        chars = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i, c in enumerate(alphabet):
            chars[c] = str(i + 1)

        curr = ""
        for c in s:
            curr += chars[c]
        curr = int(curr)
        
        while k:
            curr = toSum(str(curr))
            k -=1
        
        return curr

'''
TLDR: Use chars to keep track of conversions between the alphabet numbers + integers. Every conversion thereafter will be between str(int) and int.

TC O(n + klogn) -> klogn due to the "toSum"
SC O(logn) -> str <-> int conversion costs klogn. 
'''
