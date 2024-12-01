
#!/usr/bin/python3
import re
def process_input(filepath):
  with open(filepath, 'r') as f:
    lines = f.readlines()
    l = []
    r = []
    for line in lines:
      lr = line.split()
      l.append(int(lr[0]))
      r.append(int(lr[1]))
    l.sort()
    r.sort()
    return (l, r)

def part_one(path):
  l, r = process_input(path)
  dist = 0
  for i in range(len(l)):
    dist += abs(l[i] - r[i])
  return dist


def part_two(path):
  l, r = process_input(path)
  current = 0
  tmp = 0
  output = 0
  for i in range(len(l)):
    if l[i] != current:
      current = l[i]
      tmp = current * r.count(current)
    output += tmp 
  return output


if __name__ == '__main__':
  input = './input.txt'
  test = './test_input.txt'
  print('-- Part One --')
  print(part_one(input))
  print('-- Part Two --')
  print(part_two(input))