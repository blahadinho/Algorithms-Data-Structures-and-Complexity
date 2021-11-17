import fileinput
import time
from collections import defaultdict, deque


def find(node, parent):
    p = node
    while parent[p] != None:
        p = parent[p]
    while parent[node] != None:
        w = parent[node]
        parent[node] = p
        node = w
    return p


def union(f1, f2, parent, size):
    u = f1
    v = f2
    if size[u]<size[v]:
        parent[u] = v
        size[v] = size[v] + size[u]
    else:
        parent[v] = u
        size [u] = size[u] + size[v]



def kruskal(edges, parent, size):
    time = 0
    
    sorted_edges = deque(sorted(edges, key=lambda e:edges[e][2]))
    #print(sorted_edges)
    #print(sorted_edges.popleft())
    while sorted_edges:
        newEdge = edges[sorted_edges.popleft()]
        f1 = find(newEdge[0], parent)
        f2 = find(newEdge[1], parent)
        if f1 != f2:
            #print(4)
            union(f1, f2, parent, size)
            time += newEdge[2]
            

    print(time)

        

    



file = fileinput.input()
start_time = time.time()
i = 0
first = True
#pairs = defaultdict(list)
#weigth = defaultdict(list)

edges = dict()
j = 0
for line in file:
    line = line.strip('\n').split(' ')
    for nbr in line:
        nbr = int(nbr)
        if i == 0:
            if first:
                N = nbr #nbr of people at event
                parent = {i: None for i in range(1,N+1)}
                size = {i: 1 for i in range(1,N+1)}
                #print(1)
                first = False
            else:
                M = nbr #nbr of pairs
                i = 1
        else:
            if i == 1:
                person1 = nbr
                i = 2
            elif i == 2:
                person2 = nbr
                i = 3
            elif i == 3:
                #weigth[(person1, person2)] = nbr
                #weigth[(person2, person1)] = nbr
                #pairs[person1].append(person2)
                #pairs[person2].append(person1)
                edges[j] = [person1, person2, nbr]
                j += 1
                i = 1
#print(2)
#print("--- %s seconds ---" % (time.time() - start_time))
kruskal(edges, parent, size)
#print("--- %s seconds ---" % (time.time() - start_time))
