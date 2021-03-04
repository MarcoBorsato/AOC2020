import re
import numpy as np


def seats(data):
    input = data.read().splitlines()
    count = 0

    seats = np.zeros((128, 8), dtype=int)

    for i in input:
        row = 0
        col = 0
        rowRange = [0, 127]
        colRange = [0, 7]
        while rowRange[0] != rowRange[1]:
            for j in i:
                if j == "F":
                    rowRange = [rowRange[0], np.floor(np.nanmean([rowRange[1], rowRange[0]]))]
                if j == "B":
                    rowRange = [np.ceil(np.nanmean([rowRange[1], rowRange[0]])), rowRange[1]]
                if j == "R":
                    colRange = [np.ceil(np.nanmean([colRange[1], colRange[0]])), colRange[1]]
                if j == "L":
                    colRange = [colRange[0], np.floor(np.nanmean([colRange[1], colRange[0]]))]
        row, col = int(rowRange[0]), int(colRange[0])
        seats[row][col] = 1

    for i in range(0, 128):
        for j in range(0, 8):
            if seats[i][j] == 0:
                if j == 7:
                    if seats[i][j-1] == 1 and seats[i+1][0] == 1:
                        return i*8 + j
                if j == 0:
                    if seats[i-1][7] == 1 and seats[i][j+1] == 1:
                        return i*8 + j


    return 0
