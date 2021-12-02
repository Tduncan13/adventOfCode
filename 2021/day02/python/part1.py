#!usr/bin/env python

import sys

def main(lines):
    m = {
        'forward': 0,
        'up': 0,
        'down': 0
    }
    for line in lines:
        line = line.split()
        m[line[0]] = m[line[0]] + int(line[1])

    return m['forward'] * (m['down'] - m['up'])


if __name__ == '__main__':
    fo = open(sys.argv[1], 'r')
    lines = fo.readlines()
    print(main(lines))
    fo.close()
