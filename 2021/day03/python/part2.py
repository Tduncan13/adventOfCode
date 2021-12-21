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

    i = 0
    j = 0
    ts = ds
    while len(ts) > 1:
        tt = []
        for i in range(0, len(ts) - 1, l):
            t = ts[i:i + l - 1]
            if t[j] == gamma[j]:
                tt.append(t)
        ts = tt       

    ogr = int(''.join(ts), 2)

    ts = ds
    while len(ts) > 1:
        tt = []
        for i in range(0, len(ts) - 1, l):
            t = ts[i:i + l - 1]
            if t[j] == epsilon[j]:
                tt.append(t)
        ts = tt       

    csr = int(''.join(ts), 2)

    return ogr * csr

if __name__ == '__main__':
    fo = open(sys.argv[1], 'r')
    lines = fo.readlines()
    print(solve(lines))
    fo.close()
    
