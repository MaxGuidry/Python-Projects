
def retrace(n):
    path = []
    while n.parent is not None:
        path.append(n)
        n = n.parent
    return path


def dist(c, n):
    return 10 if c.index[0] == n.index[0] or c.index[1] == n.index[1] else 14

def mhd(n, goal):
    return abs(goal.index[0] - n.index[0])+abs(goal.index[1] - n.index[1]) * 10


def astar(start, goal):
    camefrom = []
    closed = []
    open = []
    start.h = 0
    start.g = 0
    start.f = start.g + start.h
    open.append(start)
    while open is not None:
        sorted(open, key=lambda x: x.f)
        current = open[0]
        if current == goal:
            camefrom = retrace(current)
            break
        for n in current.adjacents:
            if n in closed or n.walkable == False:
                continue
            tentative_g = n.g + dist(current, n)
            if n not in open:
                open.append(n)
            elif tentative_g >= n.g:
                continue
            n.parent = current
            n.g = tentative_g
            n.f = n.g + mhd(n, goal)
        