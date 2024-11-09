# LC 362. Design Hit Counter
class HitCounter:

    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.popleft()

        return len(self.queue)

'''
TLDR: Use queue. When getting hits, check if the first ones in queue are >= 300 seconds (past 300 seconds). If so, remove them from the queue. Return the current length of queue.

TC O(1)
SC O(N)
'''
