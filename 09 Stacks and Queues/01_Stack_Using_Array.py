class stacks:

    # CREATION OF STACK ARRAY TO STORE ITEMS
    def __init__(self):
        self.items = []   # to store data

    # CHECKING FOR EMPTY STACK
    def is_empty(self):
        return len(self.items) == 0

    # ADDING ITEM TO STACK
    def push(self, item):
        self.items.append(item)

    # REMOVING ITEM FROM STACK
    def pop(self):
        if self.is_empty():
            return "Stack Array is Empty"
        return self.items.pop()

    # CHECKING SIZE OF STACK
    def size(self):
        return len(self.items)

    # TOP (PEEK) ITEM OF STACK
    def peek(self):
        if self.is_empty():
            return "Stack Array is Empty"
        return self.items[-1]

    # STRING REPRESENTATION (IMPORTANT PART ✅)
    def __str__(self):
        return str(self.items)


# MAIN CODE
s1 = stacks()

s1.push(5)
s1.push(10)
s1.push(15)
s1.push(20)

print(f"stack content = {s1}")
