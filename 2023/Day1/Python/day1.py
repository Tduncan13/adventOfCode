#!/usr/bin/python3
import re
def process_input(filepath):
    with open(filepath, 'r') as f:
        return f.readlines()

def find_digit(line):
    nums = ['zero' , 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = []
    for i in nums:
        if line.find(i) != -1:
            digits.append(str(i))
    return int(digits[0] + digits[len(digits) - 1])



def part_one(path):
    lines = process_input(path)
    count = 0
    for line in lines:
        m = [(i, n) for i, n in enumerate(line) if n.isdigit()]
        v = m[0][1] + m[len(m) -1][1]
        count += int(v)
    return count

def part_two(path):
    lines = process_input(path)
    count = 0
    for line in lines: 
        count += find_digit(line)
    return count

if __name__ == '__main__':
    filepath = './input.txt'
    test = './test_input.txt'
    print('-- Part One --')
    print(part_one(filepath))
    print('-- Part Two --')
    print(part_two(test))