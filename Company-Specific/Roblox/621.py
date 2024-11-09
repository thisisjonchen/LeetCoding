# LC 621. Task Scheduler

# Solution from Solutions - Cred: Mayowa Daniel
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Formula: Idle_Time = Idle_Time - min(Max_freq - 1, Current_Freq)
        freq = Counter(tasks) # Counter is faster (in typing out) than using just defaultdict + loop
        freq = sorted(freq.values(), reverse = True)
        maxFreq = freq[0]
        idleTime = (maxFreq - 1) * n
        for f in freq[1:]:
            idleTime -= min(maxFreq - 1, f) # Formula
        
        idleTime = max(0, idleTime)
        return len(tasks) + idleTime

'''
TLDR: Determine the idle time

TC O(nlogn)
SC O(n)
'''
