# LC 297. Serialize and Deserialize Binary Tree
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.preorder = []
        def preorder(root):
            if not root:
                self.preorder.append("N")
                return
            self.preorder.append(str(root.val)) # str to join
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ",".join(self.preorder)
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Whereas we used dfs to perform preorder traversal, we will use it again to reverse the process
        preorder = data.split(",")
        self.i = 0
        # no need for any parameters...
        def dfs():
            if preorder[self.i] == "N":
                 self.i += 1
                 return
            node = TreeNode(preorder[self.i])
            self.i += 1 # keep progressing through the preorder
            node.left = dfs() # Attach left subtree
            node.right = dfs() # Attach right subtree
            return node           
        return dfs()


'''
TLDR: Utilize preorder to your advantage here. Notice compared to "Construct Binary Tree From Preorder And Inorder Traversal", we add the Null values via "N" to the preorder array.
We utilize these "N"s to know when to backtrack to the parent node and acts as a base case. For deserialization, we are "reversing" this process by using dfs, setting the current
node to the position of an index (i) in the preorder. We increment this i regardless of "N" or valid node value to progress through the preorder array. Finally, we return the tree.

TC O(n)
SC O(n)
'''
