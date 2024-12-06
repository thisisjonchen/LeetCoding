# LC 235. Lowest Common Ancestor of a Binary Search Tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if (p.val > root.val) and (q.val > root.val):
                root = root.right
            elif (p.val < root.val) and (q.val < root.val):
                root = root.left
            else:
                return root



'''
TLDR: Observe that the LCA is always the first node between p and q. Since this is a BST, we can go right or left if the range is not p <= root <= q.
If p and q are larger than current node, we go down the right branch (larger values). If p and q are smaller, we go down the left branch (smaller values).

TC O(log(n)) == O(height of tree)
SC O(1)... interstingly enough, the recursive version is O(1)? as well.
'''
