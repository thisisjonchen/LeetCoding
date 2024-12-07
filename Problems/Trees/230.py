# LC 230. Kth Smallest Element in a BST
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        return arr[k-1]

'''
TLDR: Use inorder traversal through the tree to obtain the already sorted values. DO NOT use .sort(), as it would result in TC O(nlogn). Return arr[k-1], due to it being 1-indexed.

TC O(n)
SC O(n) > O(h)
