#!/usr/bin/python3
import re

def does_overlap(pair_one, pair_two):
    min_one, max_one = pair_one
    min_two, max_two = pair_two
    return (min_one <= min_two <= max_one) or (min_two <= min_one <= max_two)
    

def does_fully_contain(pair_one, pair_two):
    min_one, max_one = pair_one
    min_two, max_two = pair_two
    return (min_one <= min_two and max_one >= max_two) or (min_two <= min_one and max_two >= max_one)


def part_one(filepath):
    assignments = parse_input(filepath)
    count = 0
    for pair in assignments: 
        if does_fully_contain(pair[0], pair[1]):
            count += 1
    return count

    
def part_two(filepath):
    assignments = parse_input(filepath)
    count = 0
    for pair in assignments: 
        if does_overlap(pair[0], pair[1]):
            count += 1
    return count

def parse_input(path):
    assignments = []
    with open(path, encoding='utf-8') as f:
        lines = f.read().strip().split('\n')
        for line in lines:
            a, b, c, d = map(int, re.findall(r'\d+', line))
            assignments.append([(a, b), (c, d)])
    return assignments
    
    
if __name__ == "__main__":
    test_input = './test_input.txt'
    input_path = './input1.txt'
    print("--- Part 1 ---")
    print(part_one(input_path))
    print("--- Part 2 ---")
    print(part_two(input_path))
