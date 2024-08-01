# LC 141. Linked List Cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 10**4
        if head:
            slow, fast = head, head.next
            while fast is not None:
                fast = fast.next
                count -= 1
                if count == 0:
                    slow = slow.next
                    count = 2
                if slow and fast and fast.val == slow.val and fast.next == slow.next: # make sure to include fast.next == slow.next as there are dupli vals.
                    return True
        return False

  '''
  TLDR: Use slow and fast pointers (turtle + hare) here to detect cycles. Used count at 10^4 (len of max constraint). Verify that the nodes are
  in a cycle by using next as there are duplicate values.
  TC O(n)
  SC O(1)
  ''''
