# LC 2096. Step-By-Step Directions From a Binary Tree Node to Another

# Solution from Solutions - Cred: datluu (Gave Up)
class Solution:
   def travel(self, node, target, path):
       if not node: return False
       if node.val == target: return True
       l = self.travel(node.left, target, path)
       r = self.travel(node.right, target, path)

       if l: path += ['L']
       if r: path += ['R']
       return l or r
       

   def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
       startPath, destPath = [], []
       self.travel(root, startValue, startPath)
       self.travel(root, destValue, destPath)

       while startPath and destPath and startPath[-1] == destPath[-1]:
           startPath.pop()
           destPath.pop()
       
       return "U" * len(startPath) + "".join(destPath[::-1])

  '''
  TLDR: First, the goal is to find the paths of each node (start and dest). To do so, we iterate through the tree in the travel func, using recursion to find the right node then appending to the given path list. 
  Checks if l or r. The paths should be, at index 0, from the target node to root. Thus, we pop through these paths until we come across a LCA. Once popped through, we return "U" * len(startPath) (as we are traveling up
  the tree to get to dest) and reverse the destPath as it was reversed from the recursion.
  '''
