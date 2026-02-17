class queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self,item):
        self.items.append(item)
    
    def dequeue(self):
        if len(self.items)==0:
            return "Remove nhi kar skte bcz queue already empty hai abhi"
        x=self.items.pop(0)
        return x

    def size_of_queue(self):
        return len(self.items)

    def front(self):
        if len(self.items)==0:
            return "No Front bcz queue already empty hai abhi"
        return self.items[0]

    def rear(self):
        if len(self.items)==0:
            return "No rear bcz queue already empty hai abhi"
        return self.items[-1]

