#!/usr/bin/python3

def part1(data):
    elves = []
    cal = 0
    for line in data: 
        if len(line) > 1:
            cal = cal + int(line)  
        else:
            elves.append(cal)
            cal = 0

    elves.append(cal)
    elves.sort()
    return elves[-1]



    
def part2(data):
    elves = []
    cal = 0
    for line in data: 
        if len(line) > 1:
            cal = cal + int(line)  
        else:
            elves.append(cal)
            cal = 0

    elves.append(cal)
    elves.sort()
    return elves[-1] + elves[-2] + elves[-3]

if __name__ == "__main__":
    test = './test_input.txt'
    p1 = './input1.txt'
    p2 = './input2.txt'
    data = open(p1, 'r')
    print(f"Part 1: { part1(data.readlines()) }")
    data = open(p2, 'r')
    print(f"Part 2: { part2(data.readlines()) }")
    



