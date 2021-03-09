import time


def findsum(entries: list, total: int) -> int:
    entries = [int(x) for x in entries]

    for i in entries:
        search = total - i
        if search in entries:
            return i * search


def findsum3(entries: list, total: int) -> int:
    entries = [int(x) for x in entries]

    for i in entries:
        for j in entries:
            search = total - i - j
            if search in entries:
                return i * j * search


if __name__ == '__main__':
    input = open('inputday1.txt').read().splitlines()

    print(findsum1)
