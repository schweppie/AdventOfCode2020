import pytest
import re

data_file = open('../Data/Day2.txt')
data_lines = [str(i) for i in data_file.read().splitlines()]

def SolvePart1(data_lines: str) -> int:
    passwords = 0

    for line in data_lines:
        match = re.search("(\d+)-(\d+) ([a-z]): (\w+)", line)

        min = int(match.group(1))
        max = int(match.group(2))
        character = match.group(3)
        password = match.group(4)

        count = CharacterCountInString(character, password)
        if count >= min and count <= max:
            passwords = passwords + 1

    return passwords;

def CharacterCountInString(character, string):
    count = 0
    for char in string:
        if char is character:
            count = count + 1
    return count

def SolvePart2(data_lines: str) -> int:
    passwords = 0

    for line in data_lines:
        match = re.search("(\d+)-(\d+) ([a-z]): (\w+)", line)

        min = int(match.group(1)) - 1
        max = int(match.group(2)) - 1
        character = match.group(3)
        password = match.group(4)

        if password[min] == character and password[max] != character or password[min] != character and password[max] == character:
            passwords = passwords + 1

    return passwords;

def test_example_part1():
    assert SolvePart1(["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]) == 2

def test_example_part2():
    assert SolvePart2(["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]) == 1

print (SolvePart1(data_lines))
print (SolvePart2(data_lines))
