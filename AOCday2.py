import re


def password(data):
    input = data.readlines()
    count = 0

    for i in input:
        myCount = 0
        x = re.findall('[0-9a-zA-z]+', i)
        min, max, test, str = x[0], x[1], x[2], x[3]
        times = str.count(test)

        if int(min) <= times <= int(max):
            myCount += 1

        if myCount == 1:
            count += 1

    return count

def password2(data):
    input = data.readlines()
    count = 0

    for i in input:
        x = re.findall('[0-9a-zA-z]+', i)
        min, max, test, str = int(x[0])-1, int(x[1])-1, x[2], x[3]

        if (str[min] == test) != (str[max] == test):
            count += 1

    return count