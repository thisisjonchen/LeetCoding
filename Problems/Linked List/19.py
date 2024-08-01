# LC 19. Remove Nth Node From End of List
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        count = 0

        while fast.next is not None:
            fast = fast.next
            count += 1
        
        fromEnd = count - n

        while fromEnd > 0:
            slow = slow.next
            fromEnd -= 1

        if slow.next and fromEnd == 0:
            slow.next = slow.next.next
        else:
            head = slow.next

        return head
        
'''
TLDR: Use slow + fast pointers to get count and the number from the end. If fromEnd < 0, the node that is being removed is the head.
'''
        
