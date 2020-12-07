import re

dataFile = open('../Data/Day7.txt')
dataLines = [str(i) for i in dataFile.read().splitlines()]

bagDict = {}
bagContainingGoldDict = {}
bagContainingBagsDict = {}

def PopulateBagDict():
    for i in range(len(dataLines)):
        line = dataLines[i]
        bagColor = re.match(r'(^\w+ \w+)', line).group(0)
        dataLines[i] = re.sub(r'(^\w+ \w+)( \w+ \w+)', '', line)
        bagDict[bagColor] = GetBagContents(dataLines[i], [])

def SolvePart1(dataLines: str) -> int:
    for bag in bagDict:
        bagContainingGoldDict[bag] = GetAmountOfGoldBagsOf(bag, 0)
    bagContainingGoldDict['shiny gold'] = 0
    amountOfBagsContainingGold = 0
    for bag in bagContainingGoldDict:
        if bagContainingGoldDict.get(bag) > 0:
            amountOfBagsContainingGold = amountOfBagsContainingGold + 1
    return amountOfBagsContainingGold

def GetBagContents(data: str, contents: []) -> []:
    if len(data) == 0: return contents
    match = re.match(r'^ ((\d) (\w+ \w+) \w+[,|.])', data)
    if match:
        contents.append([int(match.group(2)), match.group(3)])
        data = re.sub(r'^ ((\d) (\w+ \w+) \w+[,|.])', '', data)
    else: data = ''
    return GetBagContents(data, contents)

def GetAmountOfGoldBagsOf(bagType: str, amount: int) -> int:
    if bagType == "shiny gold":
        amount = amount + 1
    bagContents = bagDict[bagType]
    if len(bagContents) == 0: return amount
    for bag in bagContents:
        if bag[1] in bagContainingGoldDict:
            amount += bagContainingGoldDict[bag[1]] * bag[0]
        else:
            amount += GetAmountOfGoldBagsOf(bag[1], 0) * bag[0]
    return amount

def GetAmountOfBagsIn(bagType: str, amount: int) -> int:
    amount = amount + 1
    bagContents = bagDict[bagType]
    if len(bagContents) == 0: return amount
    for bag in bagContents:
        if bag[1] in bagContainingBagsDict:
            amount += bagContainingBagsDict[bag[1]] * bag[0]
        else:
            amount += GetAmountOfBagsIn(bag[1], 0) * bag[0]
    return amount

def SolvePart2(dataLines: str) -> int:
    for bag in bagDict:
        bagContainingBagsDict[bag] = GetAmountOfBagsIn(bag, 0)
    return bagContainingBagsDict['shiny gold'] - 1 # minus one, don't count self

PopulateBagDict()
print (SolvePart1(dataLines))
print (SolvePart2(dataLines))
