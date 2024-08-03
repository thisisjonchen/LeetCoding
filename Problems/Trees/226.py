# LC 226. Invert Binary Tree
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
         
        return root

  '''
  TLDR: Use recursion to set root.left to root.right, vice versa. Keep the calls going by calling the function on the left and right of root. 
  Base case if root is none.

  TC O(n)
  SC O(n) -> Can be a line of nodes (like a LL). Binary Tree only req. 2 children max, but each one can have one children resulting in O(n) worst case.
  '''
