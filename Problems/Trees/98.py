# LC 98. Validate Binary Search Tree
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # We could do in-order traversal to get the bst, then check if each value is sorted.
        tree = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            tree.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(len(tree)-1):
            if tree[i] >= tree[i+1]:
                return False
        return True


'''
TLDR: Use the property of a BST - if using inorder traversal, the resulting array will contain all the values of a BST, already sorted. We can just go through this array and check if each value is less than the next.

TC O(n)
SC O(n)
'''
