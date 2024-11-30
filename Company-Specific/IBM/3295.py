# LC 3295. Report Spam Message
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedWords = set(bannedWords) # allows for O(1) lookup time, but costs O(len(bannedWords)) space
        count = 0
        for w in message:
            if w in bannedWords:
                count += 1
            if count == 2:
                return True
        return False

'''
TLDR: Use hashset, despite "space" tradeoff, will be better than O(n^2) TC. Keep count; once count == 2, we can just return True. Else false.

TC O(n)
SC O(n)
'''
