# LC 104. Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

'''
TLDR: Have base case of root = 0. As we want the max depth, we do 1 (for the curr root) + function calls on the left and right. Use max to only get the larger side.

TC O(n)
SC O(n) -> Call Stack of Size n nodes in the tree.
'''
