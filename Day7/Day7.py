import re

dataFile = open('../Data/Day7.txt')
dataLines = [str(i) for i in dataFile.read().splitlines()]

bagDict = {}
bagContainingGoldDict = {}
bagContainingBagsDict = {}
shinyGoldKey = 'shiny gold'

def PopulateBagDict():
    for i in range(len(dataLines)):
        line = dataLines[i]
        bagColor = re.match(r'(^\w+ \w+)', line).group(0)
        dataLines[i] = re.sub(r'(^\w+ \w+)( \w+ \w+)', '', line)
        bagDict[bagColor] = GetBagContents(dataLines[i], [])

def GetBagContents(data: str, contents: []) -> []:
    if len(data) == 0: return contents
    match = re.match(r'^ ((\d) (\w+ \w+) \w+[,|.])', data)
    if match:
        contents.append([int(match.group(2)), match.group(3)])
        data = re.sub(r'^ ((\d) (\w+ \w+) \w+[,|.])', '', data)
    else: data = ''
    return GetBagContents(data, contents)

def GetAmountOfGoldBagsOf(bagType: str, amount: int) -> int:
    if bagType == shinyGoldKey:
        amount = amount + 1
    return amount + FindAmountIn(bagType, bagContainingGoldDict, GetAmountOfGoldBagsOf)

def GetAmountOfBagsIn(bagType: str, amount: int) -> int:
    return amount + FindAmountIn(bagType, bagContainingBagsDict, GetAmountOfBagsIn) + 1

def FindAmountIn(bagType: str, dataDict: {}, amountOfBagsDelegate) -> int:
    amount = 0
    bagContents = bagDict[bagType]
    for bagData in bagContents:
        if bagData[1] in dataDict:
            amount += dataDict[bagData[1]] * bagData[0]
        else:
            amount += amountOfBagsDelegate(bagData[1], 0) * bagData[0]
    return amount

def SolvePart1(dataLines: str) -> int:
    for bag in bagDict:
        bagContainingGoldDict[bag] = GetAmountOfGoldBagsOf(bag, 0)
    bagContainingGoldDict[shinyGoldKey] = 0
    amountOfBagsContainingGold = 0
    for bag in bagContainingGoldDict:
        if bagContainingGoldDict.get(bag) > 0:
            amountOfBagsContainingGold = amountOfBagsContainingGold + 1
    return amountOfBagsContainingGold

def SolvePart2(dataLines: str) -> int:
    for bag in bagDict:
        bagContainingBagsDict[bag] = GetAmountOfBagsIn(bag, 0)
    return bagContainingBagsDict[shinyGoldKey] - 1 # minus one, don't count self

PopulateBagDict()
print (SolvePart1(dataLines))
print (SolvePart2(dataLines))
