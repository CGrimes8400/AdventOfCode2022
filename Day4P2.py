listLines = []
totalCount = 0

with open("input4.txt", "r") as inputFile:   
    for line in inputFile.readlines():
        listLines.append(line)
for line in listLines:
    firstPair = line.split(",")[0]
    secondPair = line.split(",")[1]
    
    
    startFirstPair = int(firstPair.split("-")[0])
    endFirstPair = int(firstPair.split("-")[1])
    startSecondPair = int(secondPair.split("-")[0])
    endSecondPair = int(secondPair.split("-")[1])

    #if (startFirstPair >= startSecondPair and endFirstPair <= endSecondPair):
    #    totalCount += 1
#
    #elif (startSecondPair >= startFirstPair and endSecondPair <= endFirstPair):
    #    totalCount += 1
    
    if (startSecondPair <= startFirstPair <= endSecondPair):
        totalCount += 1
    elif (startSecondPair <= endFirstPair <= endSecondPair):
        totalCount += 1
    elif (startFirstPair <= startSecondPair <= endFirstPair):
        totalCount += 1
    elif (startFirstPair <= endSecondPair <= endFirstPair):
        totalCount += 1

print(totalCount)