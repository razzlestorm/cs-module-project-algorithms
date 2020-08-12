#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    #TO DO: Make sure to maximize for value
    best_ratio = sorted(items, key=lambda x: x.value/x.size)[::-1]
    # checking items in the best ratio list, will get O(n) for now, but can refactor
    knapsack = {'Value': 0, 'Chosen': []}
    for item in best_ratio:
        if capacity - item.size >= 0:
            knapsack['Chosen'].append(item.index)
            knapsack['Value'] += item.value
            capacity -= item.size
        else:
            continue
    knapsack['Chosen'] = sorted(knapsack['Chosen'])
    return knapsack


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))

    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
