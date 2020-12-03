import pytest

dataFile = open('../Data/Day1.txt')
data = [int(i) for i in dataFile.read().splitlines()]

def SolvePart1(dataList) -> int:
    for i in dataList:
        for j in dataList:
            if (i + j) == 2020:
                return i * j;

def SolvePart2(dataList) -> int:
    for i in dataList:
        for j in dataList:
            for k in dataList:
                if (i + j + k) == 2020:
                    return i * j * k;

def test_example_part1():
    assert SolvePart1([1721,979,366,299,675,1456]) == 514579

def test_example_part2():
    assert SolvePart2([1721,979,366,299,675,1456]) == 241861950

print(SolvePart1(data))
print(SolvePart2(data))
