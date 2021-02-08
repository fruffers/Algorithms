# adjacency matrix
# array of booleans
# [int node related to index][boolean connection]
# [node][node (whether there is edge to it or not)]
# you can also fill the 2nd part with 1 or 0 depending on whether there is connection between
# both indexes of nodes
adjMatrixGraph = [[False for i in range(10)] for a in range(10)]
print(adjMatrixGraph)


# adjacency list
# useful for sparse graphs (less edges than n^2)
# use a chained list where the nodes are the indexes of the buckets and the 
# chain array is the edges
# aka a list of lists
# the indexes can be Node types rather than integers if needed
# dictionary of vertices and (set of) edges
adjListGraph = { 'A':set(['B','C']),
                'B':set(['A','B','C'])}

