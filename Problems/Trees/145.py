# LC 145. Binary Tree Postorder Traversal
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def traverse(root, res):
            if not root:
                return
            traverse(root.left, res)
            traverse(root.right, res)
            res.append(root.val)
        traverse(root, self.res)
        return self.res

'''
TLDR: Recursively traverse through the tree, appending to the res in postorder (l, r, root).

TC O(n)
SC O(n)
'''
            
