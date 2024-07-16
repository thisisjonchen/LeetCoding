# LC 700. Search in a Binary Search Tree
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root != None and (root.left != None or root.right != None):
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            else:
                return root

        if root != None and root.val == val:
            return root
        return None
  '''
  TLDR: Ensure root is not None and while root.left OR root.right is not None, we go through the tree. Once we approach the node we return. Also have a conditional to check for leaves (nodes without children). Return None after.
  '''
