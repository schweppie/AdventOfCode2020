import re

dataFile = open('../Data/Day10.txt')
dataLines = [str(i) for i in dataFile.read().splitlines()]

def SolvePart1(dataLines: str) -> int:
    adapters = []
    for line in dataLines:
        adapters.append(int(line))
    adapters.sort()
    jolts = [[],[]]
    for i in range(0, len(adapters)):
        adapter = adapters[i]
        if i == 0:
            jolts[0].append(adapter)
            continue
        prevAdapter = adapters[i-1]
        if adapter - prevAdapter == 1:
            jolts[0].append(adapter)
        else:
            jolts[1].append(adapter)
        if i == len(adapters) - 1:
            jolts[1].append(adapter + 3)
    return len(jolts[0]) * len(jolts[1])

def SolvePart2(dataLines: str) -> int:
    adapters = []
    adapters.append(0)
    for line in dataLines:
        adapters.append(int(line))
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    adapterCount = len(adapters)
    arrangements = 1
    index = 0
    joltgroup = []
    lastNumber = 0
    while index < adapterCount:
        number = adapters[index]
        delta = number - lastNumber
        if delta == 3:
            branches = FindBranches( joltgroup[0], joltgroup)
            arrangements *= max(1, branches)
            joltgroup = []
        joltgroup.append(number)
        index += 1
        lastNumber = number
    return arrangements

def FindBranches(number, joltGroup) -> int:
    branches = 0
    groupCount = len(joltGroup)
    if number == joltGroup[-1]:
        return 1
    if number not in joltGroup:
        return 0
    branches += FindBranches(number + 1, joltGroup)
    branches += FindBranches(number + 2, joltGroup)
    branches += FindBranches(number + 3, joltGroup)
    return branches

print (SolvePart1(dataLines))
print (SolvePart2(dataLines))
