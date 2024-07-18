# 1530. Number of Good Leaf Nodes Pairs | Daily LC - 7/18/24

# Attempted - 7/18/24
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaves = []
        
        # identify leaves using BFS
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left or curr.right:
                if curr.left: stack.append(curr.left)
                if curr.right: stack.append(curr.right)
            else: 
                leaves.append(curr.val)

        # use DFS to track root to path. If found, we remove the node (to avoid reproducing duplicates)
        def dfs(node, path, target):
            if not node:
                return False
            if node.val == target and node.left is None and node.right is None:
                return True
            l = dfs(node.left, path, target)
            r = dfs(node.right, path, target)
            if l: 
                path += [node.left]
                if node.left == target:
                    node.left = None
            if r: 
                path += [node.right]
                if node.right == target:
                    node.right = None
            return l or r

        # store paths non-discriminately
        rootPaths = []
        for val in leaves:
            rootToLeaf = []
            dfs(root, rootToLeaf, val)
            rootPaths.append(rootToLeaf)

        # do comparisons to first find LCA then good pairs
        res = 0
        for i in range(len(rootPaths) - 1):
            for j in range(i + 1, len(rootPaths)):
                curr = rootPaths[i].copy()
                compare = rootPaths[j].copy()
                while curr[-1] == compare[-1] and len(curr) != 1 and len(compare) != 1:
                    curr.pop()
                    compare.pop()
                if len(curr) + len(compare) <= distance:
                    res += 1
        return res

# Solution - Cred: Claude
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        
        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Count good pairs
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.result += 1
            
            # Return distances to parent
            return [d + 1 for d in left + right if d + 1 < distance]
        
        dfs(root)
        return self.result

'''
TLDR: Use one pass DFS to count nodes and leaves. [d + 1 for d in left + right if d + 1 < distance] includes +1 for the parent, and left + right is the "merging" of the two arrays.
'''




