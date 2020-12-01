data_file = open('../Data/Day1.txt')
data_list = [int(i) for i in data_file.read().splitlines()]

def Part1():
    for i in data_list:
        for j in data_list:
            if (i + j) == 2020:
                print(i * j)
                return;

def Part2():
    for i in data_list:
        for j in data_list:
            for k in data_list:
                if (i + j + k) == 2020:
                    print(i * j * k)
                    return;

Part1()
Part2()
