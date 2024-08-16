# LC 860. Lemonade Change | LC Daily - 8/15/24
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}
        for c in bills:
            if c == 5: 
                change[5] += 1
            elif c == 10: 
                if change[5]:
                    change[5] -= 1
                    change[10] += 1
                else:
                    return False
            elif c == 20:
                if (change[5] and change[10]):
                    change[5] -= 1
                    change[10] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False
        return True

'''
TLDR: Simply check for conditionals. 5 => No change, 10 => Always 5, 20 => 5 and 10 OR 3 5s.

TC O(n)
SC O(3) => O(1)
'''
