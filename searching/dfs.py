# straight down then traverse back up and continue
# can use recursion or stack of nodes
# need to keep record of set of visited nodes (one might use an array of booleans)


# adj matrix n*n 
graph = [[True for i in range(10)] for j in range(10)]
visited = [False for i in range(10)]

def dfs(graph,visited,node):
    visited[node] = True
    for i in range(len(graph)):
        # visit first neighbour
        if graph[node][i] == True and visited[i] != True:
            dfs(graph,visited,i)

print(graph)