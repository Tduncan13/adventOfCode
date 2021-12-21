#!usr/bin/env python

import sys

def solve(data):
    l = len(data[0]) - 1
    count = [0] * l
    ds = ''.join(lines).replace('\n', '')
    i = 0
    for c in ds:
        idx = i % l
        count[idx] = count[idx] + 1 if c == '0' else count[idx]
        i = i + 1 
    
    g = [] 
    e = []

    for c in count:
        if c < len(data) // 2:
            g.append('1')
            e.append('0')
        else: 
            g.append('0')
            e.append('1')

    gamma = ''.join(g)
    epsilon = ''.join(e)

    return int(gamma, 2) * int(epsilon, 2)

if __name__ == '__main__':
    fo = open(sys.argv[1], 'r')
    lines = fo.readlines()
    print(solve(lines))
    fo.close()
    
