
from A_Star_Search import AStar



map = [
    [1,1,1,1,1,1,1],
    [1,1,1,0,1,1,1],
    [1,1,1,0,1,1,1],
    [1,1,1,0,1,1,1],
    [1,0,1,0,1,1,1],
    [1,1,1,1,1,1,1]
]
size = len(map)
start = (3,1)
target = (4,5)
astar = AStar(map,size,start,target)

print astar.Search()
