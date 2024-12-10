# LC 124. Binary Tree Maximum Path Sum
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        Perform BFS? 

        If we are considering both leftSubtree and rightSubtree paths, we must include root
        Disregard negative paths using max(..., 0)

        '''
        # float('-inf') to allow anything
        self.maxSum = float('-inf')
        def bfs(root):
            if not root:
                return 0
            l = max(bfs(root.left), 0)
            r = max(bfs(root.right), 0)

            maxPath = max(root.val + l + r, self.maxSum)
            self.maxSum = max(maxPath, self.maxSum)
            return root.val + max(l,r)
        bfs(root)
        return self.maxSum

  '''
  TLDR: Use BFS to traverse and compute max sum. 
  For negative paths, we set it to 0, but we are still considering negative nodes due to the returning root.val + max(l,r).

  TC O(n)
  SC O(n)
  '''
