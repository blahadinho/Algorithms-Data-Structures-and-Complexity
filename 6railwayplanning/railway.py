import fileinput
import decimal
import copy
import math
from collections import deque


def BFS(paths, cap, s, t, F, parent, mF, bfs):
    while len(bfs) > 0:
        u = bfs.pop(0)
        for v in paths[u]:
            if cap[u, v] - F[u][v] > 0 and parent[v] == -1:
                parent[v] = u
                mF[v] = min(mF[u], cap[u, v] - F[u][v])
                if v != t:
                    bfs.append(v)
                else:
                    return mF[t], parent
    return 0, parent


def networkFlow(N, M, C, paths, cap, reEdges, edges):
    i = 0
    s = 0
    t = N - 1
    flow = 0
    F = [[0 for y in range(N)] for x in range(N)]
    while flow < C:
        while True:
            parent = [-1 for x in range(N)]
            parent[s] = -2
            mF = [0 for x in range(N)]
            mF[s] = decimal.Decimal('Infinity')
            bfs = []
            bfs.append(s)
            pathF, parent = BFS(paths, cap, s, t, F, parent, mF, bfs)
            if pathF == 0:
                edge = edges[reEdge.pop()]
                paths[edge[0]].add(edge[1])
                paths[edge[1]].add(edge[0])
                i += 1
                break
            flow = flow + pathF
            v = t
            while v != s:
                u = parent[v]
                F[u][v] = F[u][v] + pathF
                F[v][u] = F[v][u] - pathF
                v = u
    return flow, i
    



file  = fileinput.input()

firstLine = file.readline()
firstLine = firstLine.strip('\n').split(' ')
N = int(firstLine[0])
M = int(firstLine[1])
C = int(firstLine[2])
P = int(firstLine[3])

edges = dict()
paths = dict()
cap = dict()
for i in range(M):
    line = file.readline()
    line = line.strip('\n').split(' ')
    edges[i] = [int(line[0]), int(line[1]), int(line[2])]
    
    if int(line[0]) not in paths:
        paths[int(line[0])] = {int(line[1])}
    else:
        paths[int(line[0])].add(int(line[1]))
    if int(line[1]) not in paths:
        paths[int(line[1])] = {int(line[0])}
    else: 
        paths[int(line[1])].add(int(line[0]))

    if (int(line[0]), int(line[1])) in cap:
        cap[(int(line[0]), int(line[1]))].append(int(line[2]))
        cap[(int(line[1]), int(line[0]))].append(int(line[2]))
    else:
        cap[(int(line[0]), int(line[1]))] = (int(line[2]))
        cap[(int(line[1]), int(line[0]))] = (int(line[2]))

reEdge = deque()
for i in range(P):
    line = file.readline()
    reEdge.append(int(line))

reEdge_temp = copy.deepcopy(reEdge)
for j in range(P):
    first = reEdge_temp.popleft()
    removeEdge = edges[first]
    paths[removeEdge[0]].discard(removeEdge[1])
    paths[removeEdge[1]].discard(removeEdge[0])

flow, i = networkFlow(N, M, C, paths, cap, reEdge, edges)


# i = 0
# flow = networkFlow(N, M, paths, cap)
# result = flow
# reEdge_temp = copy.deepcopy(reEdge)
# paths_temp = copy.deepcopy(paths)
# startRe = 0
# stopRe = P/2
# while True:
#     if (stopRe - startRe) <= 1:
#         break
#     for j in range(0, math.floor(stopRe)):
#         first = reEdge_temp.popleft()
#         removeEdge = edges[first]
#         paths_temp[removeEdge[0]].discard(removeEdge[1])
#         paths_temp[removeEdge[1]].discard(removeEdge[0])
#     result = flow
#     flow = networkFlow(N, M, paths_temp, cap)
#     if flow < C:
#         flow = result
#         paths_temp = copy.deepcopy(paths)
#         reEdge_temp = copy.deepcopy(reEdge)
#         stopRe = stopRe - (P-stopRe)/2 
#     else:
#         result = flow
#         startRe = stopRe
#         stopRe = stopRe + (P-stopRe)/2
#         paths_temp = copy.deepcopy(paths)
#         reEdge_temp = copy.deepcopy(reEdge)
#     i += 1
# print(stopRe)

print(str(P-i+1) + " " + str(flow))