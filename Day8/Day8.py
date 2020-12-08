import re

dataFile = open('../Data/Day8.txt')
dataLines = [str(i) for i in dataFile.read().splitlines()]

index = 0
accumulator = 0

def SolvePart1(dataLines: str) -> int:
    passedInstructionsDict = {}
    instructions = GetInstructions(dataLines)
    while index not in passedInstructionsDict:
        passedInstructionsDict[index] = passedInstructionsDict.get(index, 0) + 1
        instruction = instructions[index]
        method = eval(instruction[0])
        method(instruction[1])
    return accumulator

def GetOutputOf(instructions: []) -> []: # returns [ succes, accumulator]
    global index
    global accumulator
    index = 0
    accumulator = 0
    passedInstructionsDict = {}
    while index < len(instructions):
        passedInstructionsDict[index] = passedInstructionsDict.get(index, 0) + 1
        if passedInstructionsDict[index] > 1:
            return [False, 0]
        instruction = instructions[index]
        method = eval(instruction[0])
        method(instruction[1])
    return [True, accumulator]

def nop(amount: int):
    global index
    index += 1

def acc(amount: int):
    global index
    global accumulator
    index += 1
    accumulator += amount

def jmp(amount: int):
    global index
    index += amount

def SolvePart2(dataLines: str) -> int:
    table = PopulateInstructionSolutions(dataLines)
    for entry in table:
        output = GetOutputOf(entry)
        if output[0] == True:
            return output[1]
    return 0

def GetInstructions(dataLines: str) -> []:
    instructions = []
    for line in dataLines:
        match = re.match(r'(\w+) ([-+]\d+)', line)
        instructions.append([match.group(1), int(match.group(2))])
    return instructions

def PopulateInstructionSolutions(dataLines: str) -> []:
    instructionListCollection = []
    for i in range(len(dataLines)):
        match = re.match(r'(\w+) ([-+]\d+)', dataLines[i])
        if match.group(1) == "nop":
            instructionList = GetInstructions(dataLines)
            instructionList[i][0] = "jmp"
            instructionListCollection.append(instructionList)
        if match.group(1) == "jmp":
            instructionList = GetInstructions(dataLines)
            instructionList[i][0] = "nop"
            instructionListCollection.append(instructionList)
    return instructionListCollection

print (SolvePart1(dataLines))
print (SolvePart2(dataLines))
