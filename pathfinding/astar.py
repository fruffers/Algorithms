# get from point a to b
# f = g + h
# g = movement cost to square
# h = movement cost to final destination square (heuristic)
# process every node according to these values and find the most suitable

# make open list and put starting node on it with f = 0
# make closed list
# while open list not empty find node with least f on open list this is called q
# pop q off open list
# generate 8 q successors and set their parent to q
# for each successor, if successor is goal stop, 
# successor.g = q.g + distance between successor and q
# sucessor.h = distance between sucessor and goal (can use manhattan, diagonal, or euclidean heuristics)
# sucessor.f = successor.g + successor.h
