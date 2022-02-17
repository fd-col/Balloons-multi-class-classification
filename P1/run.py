# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
ec = search.GPSProblem('E', 'C'
                       , search.romania)
fd = search.GPSProblem('F', 'D'
                       , search.romania)
ap = search.GPSProblem('A', 'P'
                       , search.romania)
zf = search.GPSProblem('Z', 'F'
                       , search.romania)

#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())
print(search.branch_and_bound_search(ab)[0].path(), " visited: ", search.branch_and_bound_search(ab)[1])
print(search.heuristic_search(ab)[0].path(), " visited: ", search.heuristic_search(ab)[1])

print(search.branch_and_bound_search(ec)[0].path(), " visited: ", search.branch_and_bound_search(ec)[1])
print(search.heuristic_search(ec)[0].path(), " visited: ", search.heuristic_search(ec)[1])

print(search.branch_and_bound_search(fd)[0].path(), " visited: ", search.branch_and_bound_search(fd)[1])
print(search.heuristic_search(fd)[0].path(), " visited: ", search.heuristic_search(fd)[1])

print(search.branch_and_bound_search(zf)[0].path(), " visited: ", search.branch_and_bound_search(zf)[1])
print(search.heuristic_search(zf)[0].path(), " visited: ", search.heuristic_search(zf)[1])


print(search.branch_and_bound_search(ap)[0].path(), " visited: ", search.branch_and_bound_search(ap)[1])
print(search.heuristic_search(ap)[0].path(), " visited: ", search.heuristic_search(ap)[1])

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

