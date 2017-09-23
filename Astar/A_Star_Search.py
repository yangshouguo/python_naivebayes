

# A* To Search the way from start to end point
# H Function : Manhattan distance
class AStar(object):


    def __init__(self, Graph_Matrix, size ,startpoint, targetpoint):
        self._G = Graph_Matrix #
        self._size = size #
        self._startp = startpoint #
        self._target = targetpoint #
        self._close = [] #
        self._visit = []
        self._now = () #
        self._MHD = []
        self._direction = [(-1,0),(1,0),(0,-1),(0,1)]


    def _ManhattanDistance(self, point_now):
        return abs(point_now[1]-self._target[1])+abs(point_now[0]-self._target[0])


    def _ComputeH(self):
        for i in range(self._size):
            self._MHD.append([])
            for j in range(self._size):
                self._MHD[i].append(self._ManhattanDistance((i,j)))



    def _inmap(self, p):
        if (p[0]>=0 and p[0]< self._size and p[1]>=0 and p[1]< self._size):
            return True

        return False

    def Search(self):
        # self._ComputeH()

        self._close.append(self._startp)

        self._now = self._startp
        self._next = ()
        while (True):
            self._next = ()
            minMHT = self._size+self._size+2
            tmp = None
            for item in self._direction:
                self._next = (self._now[0]+item[0], self._now[1]+item[1])
                if (self._next in self._visit):
                    continue
                if (self._inmap(self._next) and self._G[self._next[0]][self._next[1]]==1 and self._next not in self._close):
                    if self._ManhattanDistance(self._next) < minMHT :
                        minMHT = self._ManhattanDistance(self._next)
                        tmp = self._next
            if (tmp):
                self._visit.append(tmp)
                self._close.append(tmp)
                self._now = tmp
            else:#backtrace
                pass
                self._close.pop()
                if (len(self._close)>0):
                    self._now = self._close[len(self._close)-1]
                else:
                    break
                # break

            if (tmp == self._target):
                break

        return self._close


