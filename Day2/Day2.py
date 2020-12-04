import pytest
import re

dataFile = open('../Data/Day2.txt')
dataLines = [str(i) for i in data_file.read().splitlines()]

def SolvePart1(dataLines: str) -> int:
    passwords = 0
    for line in dataLines:
        min, max, character, password = GetPasswordData(line)
        count = CharacterCountInString(character, password)
        if count >= min and count <= max:
            passwords = passwords + 1
    return passwords

def SolvePart2(dataLines: str) -> int:
    passwords = 0
    for line in dataLines:
        min, max, character, password = GetPasswordData(line)
        if IsPasswordValid(min-1, max-1, character, password):
            passwords = passwords + 1
    return passwords

def IsPasswordValid(firstIndex, secondIndex, character, password) -> bool:
    if password[firstIndex] == character and password[secondIndex] != character:
        return True
    if password[firstIndex] != character and password[secondIndex] == character:
        return True
    return False

def CharacterCountInString(character, string) -> int:
    count = 0
    for char in string:
        if char is character:
            count = count + 1
    return count

def GetPasswordData(line: str):
    # RegEx Format for '8-9 l: lzllllldsl'
    # First number   (\d+)-
    # Second number        (\d+)
    # Character                 ([a-z]):
    # Password                           (\w+)
    match = re.search(r'(\d+)-(\d+) ([a-z]): (\w+)', line)
    min = int(match.group(1))
    max = int(match.group(2))
    character = match.group(3)
    password = match.group(4)
    return min, max, character, password

def test_example_part1():
    assert SolvePart1(["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]) == 2

def test_example_part2():
    assert SolvePart2(["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]) == 1

print (SolvePart1(data_lines))
print (SolvePart2(data_lines))
