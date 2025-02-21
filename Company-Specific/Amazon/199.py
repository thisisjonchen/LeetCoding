# LC 199. Binary Tree Right Side View
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def rightView(root, level):
            if not root:
                return
            if len(res) == level:
                res.append(root.val)
            rightView(root.right, level + 1)
            rightView(root.left, level + 1)
            return
        rightView(root, 0)
        return res
