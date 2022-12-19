
mainDictionary = {}


stackOne = []
stackTwo = []
stackThree = []
stackFour = []
stackFive = []
stackSix = []
stackSeven = []
stackEight = []
stackNine = []

mainDictionary.update({1: stackOne})
mainDictionary.update({2: stackTwo})
mainDictionary.update({3: stackThree})
mainDictionary.update({4: stackFour})
mainDictionary.update({5: stackFive})
mainDictionary.update({6: stackSix})
mainDictionary.update({7: stackSeven})
mainDictionary.update({8: stackEight})
mainDictionary.update({9: stackNine})

stackInput = []



with open("input5.txt", "r") as inputFile:
       
    for line in inputFile.readlines():
        if (len(line) == 36):
            stackInput.append(line)
        elif (len(line) == 1):
            while len(stackInput) != 0:
                currentInput = stackInput.pop()
                if(currentInput[1] != " "):
                    stackOne.append(currentInput[1])
                if(currentInput[5] != " "):
                    stackTwo.append(currentInput[5])
                if(currentInput[9] != " "):
                    stackThree.append(currentInput[9])
                if(currentInput[13] != " "):
                    stackFour.append(currentInput[13])
                if(currentInput[17] != " "):
                    stackFive.append(currentInput[17])
                if(currentInput[21] != " "):
                    stackSix.append(currentInput[21])
                if(currentInput[25] != " "):
                    stackSeven.append(currentInput[25])
                if(currentInput[29] != " "):
                    stackEight.append(currentInput[29])
                if(currentInput[33] != " "):
                    stackNine.append(currentInput[33])
            #print(stackOne)
            #print(stackTwo)
            #print(stackFive)
        elif(len(line) == 0):
            print(line)
        else:
            currentLineList = line.split()
            amountToMove = int(currentLineList[1])
            moveFrom = int(currentLineList[3])
            moveTo = int(currentLineList[5])
            print(amountToMove)

            totalMoved = 0
            stackFrom = mainDictionary[moveFrom]
            stackTo = mainDictionary[moveTo]
            print(stackFrom)
            print(stackTo)
            while totalMoved < amountToMove:
                movingItem = stackFrom.pop()
                stackTo.append(movingItem)
                totalMoved += 1
            print(stackFrom)
            print(stackTo)
    print(stackOne)
    print(stackTwo)
    print(stackThree)
    print(stackFour)
    print(stackFive)
    print(stackSix)
    print(stackSeven)
    print(stackEight)
    print(stackNine)
