from collections import defaultdict
graph = defaultdict(list)

def bfs(start):
    visited = [False] * (max(graph) + 1)
    queue = []

    # queue start node and visit
    queue.append(start)
    visited[start] = True

    # keep traversing while nodes get enqued
    while queue:
        # pop the first node
        start = queue.pop()
        print(start)
        # visit all adjacent nodes and enqueue them
        for i in graph[start]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
