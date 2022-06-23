import heapq


class priorityQueue:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)[1]

    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False

    def check(self):
        print(self.cities)


class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)





def makedict(C1,C2,d):
    romania = {}

    j=0
    for i in C1:
       
        ct1 = C1[j]
        ct2 = C2[j]
        dist = d[j]
        j=j+1
        romania.setdefault(i, []).append(ctNode(ct2, dist))
        romania.setdefault(ct2, []).append(ctNode(i, dist))
    return romania


def makehuristikdict(C1,L):
    h = {}
    j=0
    for i in C1:
            
            node = i
            sld = L[j]
            h[node] = sld
            j=j+1
    return h


def heuristic(node, values):
    return values[node]


def astar(start, end,C1,C2,dist,SS,L):
    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict(SS,L)
    romania=makedict(C1,C2,dist)

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []
    print(start)

    while (q.isEmpty() == False):
        current = q.pop()
        expandedList.append(current)

        if (current == end):
            break

        for new in romania[current]:
            g_cost = distance[current] + int(new.distance)

            # print(new.city, new.distance, "now : " + str(distance[current]), g_cost)

            if (new.city not in distance or g_cost < distance[new.city]):
                distance[new.city] = g_cost
                f_cost = g_cost + heuristic(new.city, h)
                q.push(new.city, f_cost)
                path[new.city] = current
    printoutput(start, end, path, distance, expandedList)
    return path,distance,expandedList

    #


def printoutput(start, end, path, distance, expandedlist):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    
    return finalpath


