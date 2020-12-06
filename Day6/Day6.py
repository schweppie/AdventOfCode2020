import pytest
import re

dataFile = open('../Data/Day6.txt')
data = [i for i in dataFile.read().splitlines()]

def SolvePart1(dataList) -> int:
    answerSum = 0
    for answerGroup in GetAnswerGroups(dataList):
        answerSum += len(GetAnswerDict(answerGroup))
    return answerSum

def SolvePart2(dataList) -> int:
    answerSum = 0
    for answerGroup in GetAnswerGroups(dataList):
        answerDict = GetAnswerDict(answerGroup)
        peopleMatches = re.findall(r'(\w+)', answerGroup)
        peopleCount = len(peopleMatches)
        for key in answerDict:
            if answerDict[key] == peopleCount:
                answerSum += 1
    return answerSum

def GetAnswerDict(answerGroup: str) -> {}:
    answerDict = {}
    answerMatches = re.findall(r'[a-z]', answerGroup)
    for answerMatch in answerMatches:
        answerDict[answerMatch] = answerDict.get(answerMatch, 0) + 1
    return answerDict

def GetAnswerGroups(dataList) -> []:
    answerGroup = []
    answer = ""
    dataList.append("") # additional empty line eof :/ ?
    for line in dataList:
        if line == "":
            answerGroup.append(answer)
            answer = ""
        else:
            answer = answer + line + " "
    return answerGroup

print(SolvePart1(data))
print(SolvePart2(data))
