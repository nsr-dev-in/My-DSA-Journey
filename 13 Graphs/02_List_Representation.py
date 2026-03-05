n=5
m=6

edges=[[1,2],[2,4],[3,4],[1,5],[3,5],[5,4]]

#LIST
lst=[[] for i in range(n+1)]
print(lst)

for u,v in edges:
    lst[u].append(v)
    lst[v].append(u)

print(lst)
 