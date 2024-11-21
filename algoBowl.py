import math
def readFile():
    f = open("algobowl.txt", "r")
    #Vars to store 
    count = 0
    listClauses = []
    mapVariables = {}
    numberOfClauses = 0
    numberOfVariables = 0
    #For each line in file
    for line in f:
        if(count == 0):
            #First line read in counts for clauses and vars
            noNewLine = line.strip()
            listStringItems = noNewLine.split(' ')
            numberOfClauses = listStringItems[0]
            numberOfVariables = listStringItems[1]
        else:
            #all other lines are clauses
            noNewLine = line.strip()
            listStringItems = noNewLine.split(' ')
            #Turn into int
            x, y = int(listStringItems[0]), int(listStringItems[1])
            #Store clause as tuple
            listClauses.append((x,y))
            #Read through and count variables if not subtract one otherwise plus one store in dictionary where key is variable number
            if abs(x) in mapVariables.keys():
                if x > 0:
                    mapVariables[abs(x)] = mapVariables[abs(x)] + 1
                else:
                    mapVariables[abs(x)] = mapVariables[abs(x)] - 1
            else:
                if x > 0:
                    mapVariables[abs(x)] = 1
                else:
                    mapVariables[abs(x)] = -1
                
                
            if abs(y) in mapVariables.keys():
                if y > 0:
                    mapVariables[abs(y)] = mapVariables[abs(y)] + 1
                else:
                    mapVariables[abs(y)] = mapVariables[abs(y)] - 1
            else:
                if y > 0:
                    mapVariables[abs(y)] = 1
                else:
                    mapVariables[abs(y)] = -1
        count += 1
    f.close()
    return (mapVariables, listClauses)

def greedyHeuristic(mapV):
    #straight max
    listBooleans1 = []
    #reverse for every other 1,3 etc
    listBooleans2 = []
    #reverse for every other 0,2 etc
    listBooleans3 = []

    #create boolean list from max for each var
    for var in mapV:
        if mapV[var] >= 0:
            listBooleans1.append(True)
        else:
            listBooleans1.append(False)
            
    #Create every other boolean lists
    for i in range(len(listBooleans1)):
        if i % 2 == 0:
            listBooleans2.append(listBooleans1[i])
            listBooleans3.append(not(listBooleans1[i]))
        else:
            listBooleans2.append(not(listBooleans1[i]))
            listBooleans3.append(listBooleans1[i])
    
    return (listBooleans1, listBooleans2, listBooleans3)

def validation(varArr, compArr):
    count = 0
    #Loop through each clause and solve given the list of variable booleans
    for comp in compArr:
        if comp[0] > 0 and comp[1] < 0:
            if(varArr[abs(comp[0]) - 1] or not(varArr[abs(comp[1]) - 1])):
                count += 1
        elif comp[0] < 0 and comp[1] < 0:
            if(not(varArr[abs(comp[0]) - 1]) or not(varArr[abs(comp[1]) - 1])):
                count += 1
        elif comp[0] < 0 and comp[1] > 0:
            if(not(varArr[abs(comp[0]) - 1]) or varArr[abs(comp[1]) - 1]):
                count += 1
        else:
            if(varArr[abs(comp[0]) - 1] or varArr[abs(comp[1]) - 1]):
                count +=1
    return count

def main():
    fileOutputs = readFile()
    varAr = greedyHeuristic(fileOutputs[0])
    zero = validation(varAr[0], fileOutputs[1])
    one = validation(varAr[1], fileOutputs[1])
    two = validation(varAr[2], fileOutputs[1])
    scores = [zero, one, two]
    print(max(scores))
    print(varAr[scores.index(max(scores))])
if __name__ == "__main__":
    main()
