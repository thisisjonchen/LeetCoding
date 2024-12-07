# LC 102. Binary Tree Level Order Traversal
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def bfs(root, level):
            if root is None:
                return

            if len(res) < level:
                res.append([])
            res[level-1].append(root.val)

            bfs(root.left, level+1)
            bfs(root.right, level+1)
        
        level = 1
        bfs(root, level)
        return res

'''
TLDR: Here, I performed recursive bfs. However, you can use a queue to perform bfs as well. 
To do recursive bfs, we keep track of the level, and append to the respective subarray in res according to the level.

TC O(n)
SC O(n)
'''


            
