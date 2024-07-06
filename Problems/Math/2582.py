# LC 2582. Pass the Pillow | Daily - 7/6/24

# Time Complexity O(n)
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        person = 1
        next = 1
        while time > 0:
            if (person == n and next == 1) or (person == 1 and next == -1):
                next *= -1
            person += next
            time -= 1
        return person

'''
TLDR: Reverse when reaching n person or 1st person if in reverse. Could do in O(1), but since the constraints of this problem are quite small, O(n) would suffice.
'''
