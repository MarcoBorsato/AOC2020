import re
import numpy as np
import AOCday1
import AOCday2
import AOCday3
import AOCday4
import AOCday5

if __name__ == '__main__':
    input1 = open('inputday1.txt').read().splitlines()
    print(AOCday1.findsum3(input1))

    input2 = open('inputday2.txt')
    print(AOCday2.password2(input2))

    input3 = open('inputday3.txt')
    print(AOCday3.trees(input3))

    input4 = open('inputday4.txt')
    print(AOCday4.passport(input4))

    input5 = open('inputday5.txt')
    print(AOCday5.seats(input5))