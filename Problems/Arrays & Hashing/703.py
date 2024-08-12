# LC 703. Kth Largest Element in a Stream | LC Daily 8/12/24
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = sorted(nums)
        self.kth = k

    def add(self, val: int) -> int:
        self.heap += [val]
        self.heap.sort()
        return self.heap[-self.kth]
'''
TLDR: Use heap.

TC O(nlogn)
SC O(n)
'''
