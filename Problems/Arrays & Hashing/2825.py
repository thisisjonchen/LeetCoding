# LC 2825. Make String a Subsequence Using Cyclic Increments | LC Daily - 12/24/27
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # O(26) == O(1) space
        numChars = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j",
                11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s",
                20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}
        
        charNums = dict((v,k) for k,v in numChars.items())

        j = 0 # idx of str2
        for i in range(len(str1)):
            if str1[i] == str2[j]:
                j += 1
            else:
                newCharNum = charNums[str1[i]] + 1
                if newCharNum > 26: newCharNum = 1
                if numChars[newCharNum] == str2[j]:
                    j += 1
            if j == len(str2):
                return True
        return False

'''
TLDR: Use 2 dicts (O(52) == O(1)) with "two pointers" at str1, str2. Cycle only once and check if the new char matches str2, increment if needed. 
If we get to the end of str1 without getting to end of str2, then return False.

TC O(n)
SC O(1)
'''


            
        
