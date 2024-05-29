# 1492. The kth Factor of n
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, (n+2)//2): # O(n/2)
            if n % i == 0:
                factors.append(i)
        factors.append(i)
        if len(factors) < k:
            return -1
        return factors[k-1]

'''
TLDR: Only find factors in the first half--those in the second half are too large to be "factors".
'''
