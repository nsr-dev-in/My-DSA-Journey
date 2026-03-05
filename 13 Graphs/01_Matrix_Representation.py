n=5 #NODE 
m=6 #EDGES

edges=[[1,2],[2,4],[3,4],[1,5],[3,5],[5,4]]

#1 BASED INDEX GRAPH
matrix=[[0 for _ in range(n+1)] for _ in range(n+1)]
print(matrix)

for u,v in edges: #u,v 2 noode hai
    matrix[u][v] = 1
    matrix[v][u] = 1
print(matrix)

