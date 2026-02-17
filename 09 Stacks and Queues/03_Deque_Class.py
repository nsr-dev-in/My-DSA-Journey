from collections import deque

lst=deque([]) #EMPTY

lst.append(1)
lst.append(3)
lst.append(5)
lst.append(7)
lst.append(9)
lst.append(11)

print(lst)

lst.pop()
print(lst)

lst.pop()
print(lst)

lst.appendleft(1000) #STARTING ME APPEND HOGA LEFT SIDE SE
print(lst)

lst.popleft() #STARTING ME APPEND HOGA LEFT SIDE SE
print(lst)
