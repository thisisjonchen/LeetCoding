# LC 650. 2 Keys Keyboard | LC Daily - 8/19/24

# Solution from Editorial (Gave up)
class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        curr = 2 # First prime number
        while n > 1:
            while n % curr == 0:
                res += curr
                n //= curr
            curr += 1
        return res

'''
TLDR: Use prime factorization to get the min number of steps

Ex: For n = 8
> First Loop
  8 % 2 == 0
    res += 2 #res = 2
    n //= 2 #n = 4
  curr += 1 #curr = 3
  
> Second Loop
  curr += 1 #curr = 4

> Third Loop
  4 % 4 == 0
    res += 4 #res = 6
    n //= 4 #n = 1
  curr += 1 #curr = 5

exit loop since n <= 1
return res

TC O(n) => Worst case, a prime number (ex: 7, copy (1) and paste six times since there is already an initial value of "A")
SC O(1)
'''
