#!usr/bin/env python

import sys

def main(input):
    count = 0
    for i in range(0, len(input) - 3):
        a = input[i] + input[i + 1] + input[i + 2]
        b = input[i + 1] + input[i + 2] + input[i + 3]
        if a < b:
            count = count + 1
    return count

if __name__ == '__main__':
    fo = open(sys.argv[1], 'r')
    lines = fo.readlines()
    report = [int(line) for line in lines]
    print(main(report))
    fo.close()
