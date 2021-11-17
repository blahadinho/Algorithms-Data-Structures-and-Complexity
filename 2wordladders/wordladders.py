import fileinput
import time
from queue import Queue

def isEdge(word1, word2):
    i = 0
    for char in word1[1:]:
        if char in word2:
            i += 1
            word2 = word2.replace(char, "", 1)
        else: return False
    return True



def buildGraph(words):
    graph = dict()
    for word1 in words:
        for word2 in words:
            if word1 != word2 and isEdge(word1,word2):
                try:
                    graph[word1].append(word2)
                except:
                    graph[word1] = [word2]

    return graph

def distance(pred, node):
    while pred[node] != "start":
        return 1 + distance(pred, pred[node])
    return 0


def BFS(graph, words, start, end):
    pred = dict()
    pred[start] = "start"
    visited = {word: 0 for word in words}
    visited[start] = 1
    queue = Queue()
    queue.put(start)
    if start == end:
        print(distance(pred, start))
        return
    while queue.qsize() != 0:
        parent = queue.get()
        if parent in graph.keys():
            for child in graph[parent]:
                if visited[child] != 1:
                    visited[child] = 1
                    queue.put(child)
                    pred[child] = parent
                    if child == end:
                        print(distance(pred, child))
                        return
    print("Impossible")


file = fileinput.input()
#start_time = time.time()
firstLine = file.readline()
firstLine = firstLine.strip('\n').split(' ')
N = int(firstLine[0])
Q = int(firstLine[1])
words = list()

#startWords = list()
for i in range(0,N):
    words.append(file.readline().strip('\n'))


graph = buildGraph(words)
#print("--- %s seconds ---" % (time.time() - start_time))
for i in range(0,Q):
    query = file.readline().strip('\n').split(' ')
    #startWords.append(query[0])
    BFS(graph, words, query[0], query[1])
    
#print("--- %s seconds ---" % (time.time() - start_time))




