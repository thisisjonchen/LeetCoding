# LC 1381. Design a Stack With Increment Operation | LC Daily - 9/30/24
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        i = 0
        while i < k and i < len(self.stack):
            self.stack[i] += val
            i+=1


'''
TLDR: Typical stack implementation using array. There are O(1) Increment solutions using "lazy addition", will revisit.
'''
