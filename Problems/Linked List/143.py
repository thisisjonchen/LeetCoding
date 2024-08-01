# LC 143. Reorder List
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = None
            nodes.append(curr)
            curr = temp
        
        dummy = head = nodes[0]
        for i in range(1, len(nodes) // 2 + 1):
            if nodes[len(nodes)-i] == nodes[i]: # prevent duplis
                head.next = nodes[i]
                break
            head.next = nodes[len(nodes) - i]
            head = head.next
            head.next = nodes[i]
            head = head.next
        
        return dummy

'''
TLDR: First, gather all nodes in a list, making sure next is none. Then, use the pattern Li, Ln-i to reorder the list. Only need to do len(nodes) // 2 + 1.
Use a conditional to detect duplicates and break.
TC O(n)
SC O(n)
'''
