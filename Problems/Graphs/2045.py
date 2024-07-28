# LC 2045. Second Minimum Time to Reach Destination

# Solution from Solutions - Cred: B_I_T (Gave Up)
class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        dist = [[float('inf')] * 2 for _ in range(n)]
        dist[0][0] = 0
        
        q = deque([(0, 0)])
        
        while q:
            currTime, node = q.popleft()
            
            for adjNode in adj[node]:
                waitingTime = 0
                if (currTime // change) % 2 == 1:
                    waitingTime = change - (currTime % change)
                
                newTime = time + currTime + waitingTime
                
                if dist[adjNode][0] > newTime:
                    dist[adjNode][1] = dist[adjNode][0]
                    dist[adjNode][0] = newTime
                    q.append((newTime, adjNode))
                elif dist[adjNode][1] > newTime and dist[adjNode][0] < newTime:
                    dist[adjNode][1] = newTime
                    q.append((newTime, adjNode))
        
        return dist[n-1][1]

  '''
  TLDR: Will revisit.
  '''
