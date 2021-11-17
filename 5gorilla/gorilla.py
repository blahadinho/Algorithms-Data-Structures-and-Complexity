import fileinput

# def opt(i, j, word1, word2): #i och j ska vara index på bokstäverna 
    
#     if j == 0:
#         word2 = ("*" * i) + word2
#         return -4*i, word1, word2
#     if i == 0:
#         word1 = ("*" * j) + word1
#         return -4*j, word1, word2

#     letter_indx1 = alphabet[word1[i-1]]
#     letter_indx2 = alphabet[word2[j-1]]

#     if optM[i][j] != None:
#         return optM[i][j], word1, word2
    
#     road1 = opt(i-1, j-1, word1, word2)
#     road2 = opt(i, j-1, word1[:i]+'*'+word1[i:], word2)
#     road3 = opt(i-1, j, word1, word2[:j]+'*'+word2[j:])

#     roadCost1 = road1[0] + cost[letter_indx1][letter_indx2]
#     roadCost2 = road2[0] - 4
#     roadCost3 = road3[0] - 4

#     if roadCost1 == max(roadCost1, roadCost2, roadCost3):
#         optM[i][j] = roadCost1
#         return roadCost1, road1[1], road1[2]
#     elif roadCost2 == max(roadCost1, roadCost2, roadCost3):
#         optM[i][j] = roadCost2
#         return roadCost2, road2[1], road2[2]
#     elif roadCost3 == max(roadCost1, roadCost2, roadCost3):
#         optM[i][j] = roadCost3
#         return roadCost3, road3[1], road3[2]
def opt(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    for i in range(len1+1):
        for j in range(len2+1):
            letter_indx1 = alphabet[word1[i-1]]
            letter_indx2 = alphabet[word2[j-1]]
            if i == 0:
                optM[i][j] = -4*j
            elif j == 0:
                optM[i][j] = -4*i
            else:
                optM[i][j] = max(cost[letter_indx1][letter_indx2] + optM[i-1][j-1],
                                 optM[i-1][j] - 4,
                                 optM[i][j-1] - 4)
    
  
    match1 = ''
    match2 = ''
    n = len1
    m = len2
    while n > 0  and m > 0:
        letter_indx1 = alphabet[word1[n-1]]
        letter_indx2 = alphabet[word2[m-1]]
        road = optM[n][m]
        road_dia = optM[n-1][m-1]
        road_down = optM[n-1][m]
        road_left = optM[n][m-1]

        if road == (road_dia + cost[letter_indx1][letter_indx2]):
            match1 = word1[n-1] + match1
            match2 = word2[m-1] + match2
            n -= 1
            m -= 1
        elif road == (road_left - 4):
            match1 = '*' + match1
            match2 = word2[m-1] + match2
            m -= 1
        elif road == (road_down - 4):
            match1 = word1[n-1] + match1
            match2 = '*' + match2
            n -= 1
        
    if n > 0:
        match1 = word1[:n] + match1
        match2 = ('*' * n) + match2
    if m > 0:
        match1 = ('*' * m) + match1
        match2 = word2[:m] + match2
    return match1, match2





def optAlign(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    #print(opt(len1, len2, word1, word2))
    global optM
    optM = [[0 for j in range(len2+1)] for i in range(len1+1)]
    return opt(word1, word2)


file = fileinput.input()
firstLine = file.readline()
firstLine = firstLine.strip('\n').split(' ')
global alphabet
alphabet = dict()
indx = 0
for letter in firstLine:
    alphabet[letter] = indx
    indx += 1

k = len(alphabet)
global cost
cost = [[0 for x in range(k)] for y in range(k)]

for i in range(k):
    line = file.readline().strip('\n').split(' ')
    for j in range(k):
        cost[i][j] = int(line[j])

line = file.readline().strip('\n').split(' ')
nbrQ = int(line[0])

for i in range(nbrQ):
    line = file.readline().strip('\n').split(' ')
    word1 = line[0]
    word2 = line[1]
    words = optAlign(word1, word2)
    print(words[0] + " " + words[1])

