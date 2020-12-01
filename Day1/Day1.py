import pytest

data_file = open('../Data/Day1.txt')
data = [int(i) for i in data_file.read().splitlines()]

def SolvePart1(data_list) -> int:
    for i in data_list:
        for j in data_list:
            if (i + j) == 2020:
                return i * j;

def SolvePart2(data_list) -> int:
    for i in data_list:
        for j in data_list:
            for k in data_list:
                if (i + j + k) == 2020:
                    return i * j * k;

def test_example_part1():
    assert SolvePart1([1721,979,366,299,675,1456]) == 514579

def test_example_part2():
    assert SolvePart2([1721,979,366,299,675,1456]) == 241861950

print(SolvePart1(data))
print(SolvePart2(data))
