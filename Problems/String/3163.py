# LC 3163. String Compression III
class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        l, r = 0, 0
        while r < len(word):
            count = 0
            
            while r < len(word) and word[l] == word[r]:
                r += 1
                count += 1
            
            while count >= 9:
                comp += "9" + word[l]
                count -= 9
            if count > 0:
                comp += str(count) + word[l]
        
            l = r
        return comp

'''
TLDR: Use sliding window and count until new letter. Ration count accordingly with 9 (max). Add to compressed string accordingly. Then, set the left pointer to right pointer and continue.
'''
        
