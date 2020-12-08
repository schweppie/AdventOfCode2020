import re

dataFile = open('../Data/Day8.txt')
dataLines = [str(i) for i in dataFile.read().splitlines()]

index = 0
accumulator = 0
instructions = []

passedInstructionsDict = {}

class NoOperation:
    global index
    def Execute(self):
        index = index + 1
    def Revert(self):
        index = index - 1

class JumpOperation:
    global index
    def __init__(self, jump: int):
        self.jump = jump
    def Execute(self):
        index = index + self.jump
    def Revert(self):
        index = index - self.jump

class AccumulateOperation:
    global index
    def __init__(self, jump: int):
        self.jump = jump
    def Execute(self):
        index = index + self.jump
    def Revert(self):
        index = index - self.jump



def test():

    testList = [classa(), classb()]

    for item in testList:
        item.do()








def SolvePart1(dataLines: str) -> int:
    global index
    while True:
        if index in passedInstructionsDict:
            return accumulator
        passedInstructionsDict[index] = 1
        instruction = instructions[index]
        method = eval(instruction[0])
        method(instruction[1], False)
    return 0

def nop(amount: int, revert: bool):
    global index
    if revert:
        index -= 1
    else:
        index += 1

def acc(amount: int, revert: bool):
    global index
    global accumulator
    if revert:
        index -= 1
        accumulator -= amount
    else:
        index += 1
        accumulator += amount

def jmp(amount: int, revert: bool):
    global index
    if revert:
        index -= amount
    else:
        index += amount

def SolvePart2(dataLines: str) -> int:
    passedInstructionsDict = {}
    global index
    global accumulator
    index = 0
    accumulator = 0
    while True:

        if index >= len(instructions):
            return accumulator

        instruction = instructions[index]



        oldIndex = index

        method = eval(instruction[0])
        method(instruction[1], False)

        passedInstructionsDict[oldIndex] = 1

        print (str(index) + " inst: " + str(instruction) + " accu=" + str(accumulator) + " dict: " + str(passedInstructionsDict))

        x = input()

        if index in passedInstructionsDict:
            index = oldIndex
            method(instruction[1], True)

            print (str(index) + " REVERT inst: " + str(instruction) + " dict: " + str(passedInstructionsDict))
            if instruction[0] == "nop":
                instructions[index][0] = "jmp"
            elif instruction[0] == "jmp":
                instructions[index][0] = "nop"


    return 0

def PopulateInstructions(dataLines: str):
    for line in dataLines:
        match = re.match(r'(\w+) ([-+]\d+)', line)
        instructions.append([match.group(1), int(match.group(2))])
test()
PopulateInstructions(dataLines)
print (SolvePart1(dataLines))
#print (SolvePart2(dataLines))
