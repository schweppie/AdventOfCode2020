dataFile = open('../Data/Day3.txt')
dataList = [i for i in dataFile]
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
width = len(dataList[0])-1
height = len(dataList)

def SolvePart1(dataList) -> int:
    return FindTreeCollisions(dataList, 0, 0, 0, [3,1])

def FindTreeCollisions(dataList, x, y, collisions, slope) -> int:
    x = x + slope[0]
    y = y + slope[1]
    if x >= width:
        x = x - width
    if y >= height:
        return collisions
    if dataList[y][x] == "#":
        collisions = collisions + 1
    return FindTreeCollisions(dataList, x, y, collisions, slope)

def SolvePart2(dataList) -> int:
    collisionList = []
    for slope in slopes:
        collisionList.append(FindTreeCollisions(dataList, 0, 0, 0, slope))
    totalCollisions = 1
    for collisions in collisionList:
        totalCollisions = totalCollisions * collisions
    return totalCollisions

print(SolvePart1(dataList))
print(SolvePart2(dataList))
