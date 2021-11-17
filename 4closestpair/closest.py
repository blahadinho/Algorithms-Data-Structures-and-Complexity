import fileinput
import math
import time

def bruteForce(P):
    minD = math.sqrt((P[0][0] - P[1][0]) ** 2 + (P[0][1] - P[1][1]) ** 2)
    length = len(P)
    p1 = P[0]
    p2 = P[1]
    if length == 2:
        return (p1, p2, minD)
    else:
        for i in range(length-1):
            for j in range(i + 1, length):
                if i != 0 and j != 1:
                    d = math.sqrt((P[i][0] - P[j][0]) ** 2 + (P[i][1] - P[j][1]) ** 2)
                    if d < minD:
                        minD = d
                        p1 = P[i]
                        p2 = P[j]
        return(p1, p2, minD)

def closest_Boundary(Px, Py, delta, bestPair):
    mid = Px[len(Px) // 2][0]
    S = [point for point in Py if mid -delta <= point[0] <= mid + delta]

    dist = delta
    length = len(S)
    for i in range(length-1):
        for j in range(i+1, min(i+7,length)):
            p1 = S[i]
            p2 = S[j]
            dis = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
            if dis < dist:
                dist = dis
                bestPair = (p1, p2)
    return (bestPair, dist)






def closest(Px, Py, n):
    if n <= 3:
        return bruteForce(Px)
    mid = n // 2
    Lx = Px[:mid]
    Rx = Px[mid:]
    
    Ly = list()
    Ry = list()
    rx_temp = set(Rx)
    for point in Py:
        if point in rx_temp:
            Ry.append(point)
        else:
            Ly.append(point)

    (lPoint1, lPoint2, distL) = closest(Lx, Ly, mid)
    (rPoint1, rPoint2, distR) = closest(Rx, Ry, mid)

    if distL <= distR:
        delta = distL
        smallestDist = (lPoint1, lPoint2)
    else:
        delta = distR
        smallestDist = (rPoint1, rPoint2)
    
    (smallestDist, delta) = closest_Boundary(Px, Py, delta, smallestDist)

    return (smallestDist[0], smallestDist[1], delta)



file = fileinput.input()
start_time = time.time()
firstLine = file.readline()
firstLine = firstLine.strip('\n').split(' ')
N = int(firstLine[0])
points_X = list()
points_Y = list()

#startWords = list()
for i in range(0,N):
    line = file.readline().strip('\n').split(' ')
    points_X.append(int(line[0]))
    points_Y.append(int(line[1]))
#print("--- %s seconds ---" % (time.time() - start_time))
P = list(zip(points_X, points_Y))
Px = sorted(P, key=lambda points_X: points_X[0])
Py = sorted(P, key=lambda points_Y: points_Y[1])
#print("--- %s seconds ---" % (time.time() - start_time))
(closestPoint1, closestPoint2, minDist) = closest(Px, Py, N)
#print("--- %s seconds ---" % (time.time() - start_time))
print('%.6f' % minDist)
