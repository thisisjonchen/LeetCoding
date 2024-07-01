# LC 21. Merge Two Sorted Lists

# 7/1/24 | O(m+n), m -> l1, n -> l2
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = root = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                root.next = list1
                list1 = list1.next
            else:
                root.next = list2
                list2 = list2.next
            root = root.next

        if list1:
            root.next = list1
        else:
            root.next = list2

        return dummy.next

'''
TLDR: Iterate through LL until one of them empty, then set the root/curr next to the non remaining one. Use dummy for head, and use .next for the start of the merged LL.
'''
