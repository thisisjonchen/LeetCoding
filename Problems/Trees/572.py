# LC 572. Subtree of Another Tree
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if (root and not subRoot) or (not root and subRoot) or (root.val != subRoot.val):
            return False
        l = self.isSameTree(root.left, subRoot.left)
        r = self.isSameTree(root.right, subRoot.right)
        return l and r

'''
TLDR: Make sure to do 100. Is Same Tree first. If subroot is none, then the subroot can be anything (thus true). No root, not subtree so false.
We check if the root and subroots are the same at each level (height), calling recursively the left and right if not true.

TC O(n*m)
SC O(n)
'''

        

        
            

            
