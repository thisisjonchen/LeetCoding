# LC 105. Construct Binary Tree from Preorder and Inorder Traversal
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        # the first value in preorder will always be the root
        root = TreeNode(preorder[0])
        # find index of root in inorder. Left and right will be left and right respective subtrees
        indexOfRoot = inorder.index(preorder[0])
        # Utilize splicing to split the preorder + inorder
        # For inorder, note the that the leftSubtree will be everything from 0 up to the indexOfRoot (iOR exclusive)
        # The rightSubtree in inorder will be everything from indexOfRoot + 1 to end of inorder
        leftSubtreeInorder = inorder[0:indexOfRoot]
        rightSubtreeInorder = inorder[indexOfRoot+1:len(inorder)]
        # For preorder, since index 0 is the root, we take the left from 1 to number of nodes in leftSubtree. We do +1 to include the each node.
        # The right subtree in preorder will be everything from the leftSubtree + 1 to end.
        leftSubtreePreorder = preorder[1:len(leftSubtreeInorder)+1]
        rightSubtreePreorder = preorder[len(leftSubtreeInorder)+1:len(preorder)]
        
        # Now attach the left and right subtree, recursively calling buildTree to root
        root.left = self.buildTree(leftSubtreePreorder, leftSubtreeInorder)
        root.right = self.buildTree(rightSubtreePreorder, rightSubtreeInorder)

        return root
        
'''
TLDR: HIGHLY recommend drawing this one out, with at least a full binary tree (balanced, each row and subtree has the same elements).
This will help with figuring out how to splice the preorder + inorder. See notes above.

TC O(n)
SC O(n)
'''
