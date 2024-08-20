# LC 100. Same Tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q) or (p.val != q.val):
            return False
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)
        return l and r

'''
TLDR: Have conditionals checking if both are None (true) and if either are None or values do not match (false). If none of the conditionals were hit,
meaning they are indeed the same val, we continue the recursive calls on the left and right, then return l and r, checking if they do match.

'''
        
