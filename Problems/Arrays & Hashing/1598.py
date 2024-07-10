# LC 1598. Crawler Log Folder | Daily - 7/10/24
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        log = []
        for step in logs:
            if step == "../":
                if len(log) > 0:
                    log.pop()
            elif step != "./":
                log.append(step)
        return len(log)
'''
TLDR: If step is "../", pop. Else if step is anything else but "./", append to log (stack).
'''
