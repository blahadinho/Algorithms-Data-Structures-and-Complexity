import fileinput
import sys
import time
from collections import deque

def matcher(men, woman, prefsMan, prefsWoman): #Gale-Shapley algoritmen, O(n²)
    p = deque(men)
    guyMar = {guy: None for guy in men}
    girlMar = {girl: None for girl in woman}
    while p:
        guy = p.popleft()
        girl = prefsMan[guy].pop(0)
        if girlMar[girl] is None:
            girlMar[girl] = guy
            guyMar[guy] = girl
        else:
            otherGuy = girlMar[girl]
            if prefsWoman[girl][guy-1] < prefsWoman[girl][otherGuy-1]:
                p.append(otherGuy)
                girlMar[girl] = guy
                guyMar[guy] = girl
                guyMar[otherGuy] = None
            else:
                p.append(guy)

    return girlMar

file = fileinput.input()    

start_time = time.time()
woman = []
man = []
prefsMan = dict()
prefsWoman = dict()
i = -1
isMan = False

for line in file:
    for nbr in line.split(' '):
        nbr = int(nbr)
        if i == -1:
            n = nbr
            w = [0] * nbr
            i = i + 1
        else:
            
            if (i % (n+1)) == 0:
                personIndex = nbr
                if w[personIndex-1] == 0:
                    woman.append(personIndex)
                    prefsWoman[personIndex] = [None]*n
                    isMan = False
                    w[personIndex-1] = 1
                else:
                    man.append(personIndex)
                    isMan = True
            else:
                if isMan == False:
                    prefsWoman[personIndex][nbr-1] = i % (n+1)
                else:
                    prefsMan.setdefault(personIndex,[]).append(nbr)
            i = i + 1
                    
#print("--- %s seconds ---" % (time.time() - start_time))
stableMarriages = matcher(man, woman, prefsMan, prefsWoman)

for i in range(1,n+1):
    print(stableMarriages[i])

#print("--- %s seconds ---" % (time.time() - start_time))





 
 


    
