# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def findsum(numlist):
    numlist_int = [int(x) for x in numlist]

    for i in numlist_int:
        for j in numlist_int:
            if int(i) == int(j):
                continue
            else:
                if int(i) + int(j) == 2020:
                    return int(i)*int(j)

def findsum3(numlist):
    numlist_int = [int(x) for x in numlist]

    for i in numlist_int:
        for j in numlist_int:
            for k in numlist_int:
                if i == j or i == k or j == k:
                    continue
                else:
                    if (i + j + k) == 2020:
                        return i*j*k