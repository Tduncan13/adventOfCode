#!/usr/bin/python3

def calc_priority(item):
    if 65 <= ord(item) <= 90:
        return ord(item) - ord('A') + 27
    elif 97 <= ord(item) <= 122:
        return ord(item) - ord('a') + 1
    else:
        return 0

def part_one(data):
    priority_sum = 0
    for line in data: 
        mid = len(line) // 2
        common = set(line[:mid]) & set(line[mid:]) 
        priority_sum += calc_priority(common.pop())
    
    return priority_sum
    
def part_two(data):
    priority_sum = 0
    sacks = data.strip().split("\n")
    for i in range(0, len(sacks), 3):
        common = set(sacks[i]) & set(sacks[i + 1]) & set(sacks[i + 2])
        priority_sum += calc_priority(common.pop())
        
    return priority_sum

    
if __name__ == "__main__":
    test = './test_input.txt'
    p1 = './input1.txt'
    p2 = './input2.txt'
    data = open(p1, 'r')
    print("--- Part 1 ---")
    print(part_one(data.readlines()))
    data = open(p2, 'r')
    print("--- Part 2 ---")
    print(part_two(data.read()))
