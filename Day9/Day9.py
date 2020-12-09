import re

dataFile = open('../Data/Day9.txt')
dataLines = [str(i) for i in dataFile.read().splitlines()]

def SolvePart1(dataLines: str) -> int:
    preamble = 25
    for i in range(preamble, len(dataLines)):
        number = int(dataLines[i])
        sumDict = {}
        for j in range(i-preamble, i):
            for k in range(i-preamble, i):
                if j == k:
                    continue
                a = int(dataLines[j])
                b = int(dataLines[k])
                sumDict[int(a + b)] = True
        if number not in sumDict:
            return number
    return 0

def SolvePart2(dataLines: str) -> int:
    target = SolvePart1(dataLines)
    dataNumbers = []
    for line in dataLines:
        dataNumbers.append(int(line))
    startIndex = 0
    endIndex = 0
    currentSet = []
    while startIndex < len(dataNumbers):
        setSum = sum(currentSet)
        if setSum == target:
            currentSet.sort()
            return currentSet[0] + currentSet[len(currentSet)-1]
        if setSum > target:
            startIndex += 1
            endIndex = 0
            currentSet = []
        else:
            endIndex += 1
        currentSet.append(dataNumbers[startIndex + endIndex])
    return 0

print (SolvePart1(dataLines))
print (SolvePart2(dataLines))
