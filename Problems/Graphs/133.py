# LC 133. Clone Graph
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        dummy = x = Node(node.val)
        keyNodes = {node.val:x}
        queue = deque()
        queue.append(node)
        while queue:
            curr = queue.popleft()
            for n in curr.neighbors:
                if n.val not in keyNodes: # we have not seen before
                    keyNodes[n.val] = Node(n.val)
                    queue.append(n)
                keyNodes[curr.val].neighbors.append(keyNodes[n.val])
        return dummy                
        
'''
TLDR: This problem specifies that we must create a deep copy - in other words, we need to create the matching number of new nodes and
have the same neighbors, identical to the original graph. To do so, we create a new node to match the node given (with a dummy to call as return)
and then we use a queue with BFS + a dict. The queue is needed for BFS and the dict is there to check if the node already exists, add it if not, then
reference it in the new node's neighbors. We continue this until we are done with no worry of repeated edges/self loops (constraints)

TC O(V+E) -> V = verticies, E = edges
SC O(V)
'''
