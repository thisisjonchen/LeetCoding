# 1110. Delete Nodes And Return Forest - Daily 7/17/24

# Solution from Solutions - Cred: kartikdevsharmaa (Gave Up)
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete) # To allow for O(1) lookup
        forest = [] # result
        
        def dfs(node, is_root): # Use DFS, not BFS
            if not node:
                return None
            
            is_deleted = node.val in to_delete_set # Checks if root in to be deleted
            if is_root and not is_deleted: # Appends root
                forest.append(node)
            
            node.left = dfs(node.left, is_deleted)
            node.right = dfs(node.right, is_deleted)
            
            return None if is_deleted else node # Handles children after they are deleted or still exist
        
        dfs(root, True)
        return forest

  '''
  TLDR: Use DFS, recursively look through and append to the forest result. Recursively check for children, return Node if not deleted or None if so.
  '''
