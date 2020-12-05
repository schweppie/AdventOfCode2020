import re
import math

dataFile = open('../Data/Day5.txt')
dataLines = [str(i) for i in dataFile.read().splitlines()]

def SolvePart1(dataLines: str) -> int:
    return max(GetSeatIds(dataLines))

def SolvePart2(dataLines: str) -> int:
    seatIds = GetSeatIds(dataLines)
    seatIds.sort()
    lastId = seatIds[0]
    for seatId in seatIds:
        if seatId - lastId == 2:
            return seatId - 1
        lastId = seatId
    return -1

def GetSeatIds(dataLines: str) -> []:
    seatIds = []
    for line in dataLines:
        passData = re.match(r'([FB]+)([RL]+)', line)
        row = SearchPassData(passData.group(1), 0, 127, 0, "F")
        colum = SearchPassData(passData.group(2), 0, 7, 0, "L")
        seatIds.append(int(row * 8 + colum))
    return seatIds

def SearchPassData(rowData: str, start: int, end: int, depth: int, lowerChar: str) -> int:
    if depth == len(rowData):
        return start
    half = int(math.floor((end - start) * 0.5))
    if rowData[depth] == lowerChar:
        return SearchPassData(rowData, start, end - half - 1, depth + 1, lowerChar)
    else:
        return SearchPassData(rowData, start + half + 1, end, depth + 1, lowerChar)

print (SolvePart1(dataLines))
print (SolvePart2(dataLines))
