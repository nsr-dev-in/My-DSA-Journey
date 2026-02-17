class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class StackDLL:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, data):
        new_node = Node(data)

        if self.top is not None:
            new_node.next = self.top
            self.top.prev = new_node

        self.top = new_node
        print(data, "pushed")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return None

        removed = self.top.data
        self.top = self.top.next

        if self.top:
            self.top.prev = None

        return removed

    # Peek operation
    def peek(self):
        if self.top is None:
            return "Stack Empty"
        return self.top.data

    # Check empty
    def isEmpty(self):
        return self.top is None


# Example usage
s = StackDLL()

s.push(10)
s.push(20)
s.push(30)

print("Top:", s.peek())
print("Popped:", s.pop())
print("Top after pop:", s.peek())
