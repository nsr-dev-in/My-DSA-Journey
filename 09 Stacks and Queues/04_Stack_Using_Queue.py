from collections import deque

class stacks_using_queue:
    def __init__(self):
        self.queue=deque([])
    
    def push(self,value):
        self.queue.append(value)

        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft()) #first wala pick karo and append to last
        
    def pop(self):
        if len(self.queue)==0:
            return "empty hai queue"
        return self.queue.popleft()

    def peek(self):
        if len(self.queue)==0:
            return "empty hai queue"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)