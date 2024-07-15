# LC 2196. Create Binary Tree From Descriptions
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        child = set()

        for i in range(len(descriptions)):
            if not nodes.get(descriptions[i][0]):
                nodes[descriptions[i][0]] = TreeNode(descriptions[i][0])
            if not nodes.get(descriptions[i][1]):
                nodes[descriptions[i][1]] = TreeNode(descriptions[i][1])
            if descriptions[i][2] == 1:
                nodes[descriptions[i][0]].left = nodes[descriptions[i][1]]
            else:
                nodes[descriptions[i][0]].right = nodes[descriptions[i][1]]
            child.add(descriptions[i][1])

        for d in descriptions:
            parent = d[0]
            if parent not in child: # what
                return nodes[parent]

        return None

'''
TLDR: Iterate through descriptions, creating parent and child nodes (if necessary) and linking them in the same pass. Also, add to child set to find parent (parent not in child is root). O(n) time and space.
'''
            

        
        
        

         
