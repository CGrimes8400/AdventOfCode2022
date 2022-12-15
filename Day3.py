print("Hello World")

listLines = []
totalVal = 0

with open("input3.txt", "r") as inputFile:   
    for line in inputFile.readlines():
        listLines.append(line)
for line in listLines:

    
    firstHalf = line[0:int((len(line)-1)/2)]
    secondHalf = line[int((len(line)-1)/2):len(line)-1]
    #print(firstHalf)
    #print(secondHalf)
    #print(firstHalf + secondHalf)
    #print(line)
    #print(len(line))
    #print(len(firstHalf))
    #print(len(secondHalf))

    for currentChar in firstHalf:
        foundVal = secondHalf.find(currentChar)
        if  foundVal != -1:
            print(secondHalf[foundVal])

            


            numVal = ord(secondHalf[foundVal])
            if numVal <= 90:
                numVal = numVal - 64 + 26
            elif numVal >= 97:
                numVal = numVal - 96
            print(numVal)
            totalVal += numVal

            break

print(totalVal)
