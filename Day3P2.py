print("Hello World")

listLines = []
totalVal = 0
lineAlpha = ""
lineBravo = ""
lineCharlie = ""
currentLine = 1

with open("input3.txt", "r") as inputFile:   
    for line in inputFile.readlines():
        listLines.append(line)
for line in listLines:
    if (currentLine == 1):
        lineAlpha = line
    if (currentLine == 2):
        lineBravo = line
    if (currentLine == 3):
        lineCharlie = line
    currentLine+=1
    
    #firstHalf = line[0:int((len(line)-1)/2)]
    #secondHalf = line[int((len(line)-1)/2):len(line)-1]
    #print(firstHalf)
    #print(secondHalf)
    #print(firstHalf + secondHalf)
    #print(line)
    #print(len(line))
    #print(len(firstHalf))
    #print(len(secondHalf))
    if currentLine == 4:

        for currentChar in lineAlpha:
            foundValBravo = lineBravo.find(currentChar)
            foundValCharlie = lineCharlie.find(currentChar)
            if  foundValBravo != -1 and foundValCharlie != -1:
                print(currentChar)




                numVal = ord(currentChar)
                if numVal <= 90:
                    numVal = numVal - 64 + 26
                elif numVal >= 97:
                    numVal = numVal - 96
                print(numVal)
                totalVal += numVal

                break
        currentLine = 1

print(totalVal)
