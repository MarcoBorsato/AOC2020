import re

dataType = (int, int, str, str)


def convertData(line):
    found = re.findall(r'(\d+)-(\d+) (\w): (.*)', line)[0]
    return int(found[0]), int(found[1]), found[2], found[3]


def readInput(input):
    data = open('inputday2.txt').readlines()
    return [convertData(line) for line in data]


def password1(data: dataType) -> bool:
    return data[3].count(data[2]) in range(data[0], data[1] + 1)


def password2(data: dataType) -> bool:
    a = bool(data[3][data[0] - 1] == data[2])
    b = bool(data[3][data[1] - 1] == data[2])
    return a != b


def count(data):
    count1, count2 = 0, 0
    for d in readInput(data):
        if password1(d):
            count1 += 1
        if password2(d):
            count2 += 1
    return count1, count2


if __name__ == '__main__':
    inputday2 = readInput(open('inputday2.txt'))
    print(count(inputday2))
