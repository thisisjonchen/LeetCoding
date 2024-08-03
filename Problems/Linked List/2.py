# LC 2. Add Two Numbers
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        multiplier = 1
        res = 0
        while l1 and l2:
            curr = l1.val + l2.val
            res += curr * multiplier
            multiplier *= 10
            if l1 and l1.next and l2.next is None:
                l2.next = ListNode(0)
            elif l2 and l2.next and l1.next is None:
                l1.next = ListNode(0)
            l1, l2 = l1.next, l2.next

        res = str(res)
        dummy = head = ListNode()
        for i in range(len(res) - 1, -1, -1):
            head.next = ListNode(res[i])
            head = head.next
        return dummy.next

'''
TLDR: Use a multiplier to keep track of position. With that, we are adding to the total by iterating through the LLs.
If at any point the L1/2.next is None while the other exists, we sub in ListNode(0). Then, we convert the res to str (iterable) and create a new LL to return.

TC O(max(n,m)); n = l1, m = l2
SC O(max(n,m)); n = l1, m = l2
'''
