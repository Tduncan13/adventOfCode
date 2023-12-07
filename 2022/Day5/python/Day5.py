#!/usr/bin/python3
def process_input(filepath):
    with open(filepath, 'r') as f:
        return f.readlines()

def get_index(lines):
    idx = 0
    for line in lines:
        if len(line) == 1:
            break
        idx += 1
    return idx 

def get_crates(lines, idx):
    crates = []
    lines = lines[0:idx]
    stack_count = len(lines[0]) // 3
    print('Num of crate stacks')
    print(stack_count)
    return crates

def get_instructions(lines, idx):
    instructions = lines[idx:len(lines)]
    return instructions

def part_one(filepath):
    lines = process_input(filepath)
    idx = get_index(lines)
    crates = get_crates(lines, idx)
    instructions = get_instructions(lines, idx)
    
    print('*** Crates ***')
    print(crates)        
    print('*** Instructions ***')
    print(instructions)        
    
    
def part_two(filepath):
    return 'N/A'

if __name__ == '__main__':
    filepath = './input.txt'
    test = './test_input.txt'
    print('-- Part One --')
    print(part_one(test))
    print('-- Part Two --')
    print(part_two(filepath))
