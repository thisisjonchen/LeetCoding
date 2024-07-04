# LC 2181. Merge Nodes In Between Zeroes | Daily - 7/4/24
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = slow.next
        dummy = mod = ListNode()
        while fast is not None:
            if fast.val == 0:
                slow = slow.next
                curr = 0
                while slow.val != 0:
                    curr += slow.val
                    slow = slow.next
                mod.next = ListNode(curr)
                mod = mod.next
            fast = fast.next
        return dummy.next
'''
TLDR: Utilize slow and fast pointer approach, can prob do without creating a new dummy LL for results. However, O(n).
'''
