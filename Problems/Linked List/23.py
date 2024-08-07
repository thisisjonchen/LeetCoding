# LC 23. Merge K Sorted Lists
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for i in range(len(lists)-1, -1, -1): # Purge Empty Lists
            if not lists[i]:
                del lists[i]

        dummy = head = ListNode()
        while lists:
            currMin = float("inf")
            minIndex = 0
            for i in range(len(lists)): # Find min
                currNode = lists[i]
                if currNode and currNode.val < currMin:
                    currMin = currNode.val
                    minIndex = i
            
            head.next = ListNode(currMin) # Append to LL
            head = head.next

            if lists[minIndex].next is None: # Delete Empties
                del lists[minIndex]
            else:
                lists[minIndex] = lists[minIndex].next

        return dummy.next

'''
TLDR: First, purge empty LL. Then iterate through each of the currNode of LL, comparing to see which is the min (to be added to the cul LL).
If the list.next is None (meaning it is on its final node), delete it.

TC O(nk) <- Could be better at O(nlogk) using merge sort. Will increase SC to O(n) though.
SC (1)
'''
            

                

