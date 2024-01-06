# LC 125. Valid Palindrome
import re

# Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^0-9a-zA-Z]+', "", s).lower()
        for i in range (len(s)):
            if (s[i] != s[len(s) -1 -i]):
                return False
        return True
    
'''
TLDR: Remove non-alphanumeric values using regex. Compare left and right indexes moving in. If not equal, return false.

Explaination:
This problem was super easy as it basically gives us the path of converting everything to lowercase and removing
all non-alphanumeric (like * or _) from the "s" string. Using regex, this is super easy, albeit the regex for it is
weird. Then, we just compare the two ends (two pointers!) and see if it is equal all the way through. If not, return False.
'''