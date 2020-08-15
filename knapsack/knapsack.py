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

def knapsack_dynamic(values, weights, maxWeightConstraint):
    cache = [[0] * (maxWeightConstraint + 1)] * (len(values) + 1)

        for total_items in range(0, len(values) + 1):
        for max_weight in range(0, maxWeightConstraint + 1):
                '''
                I cache the name 'currentItem' for clarity when accessing values & weights, but I
                leave 'totalItems - 1' "raw" when we access the cache so you can visualize:
                    1.) Without Item -> Going up 1 row
                    2.) With Item -> Go up 1 row & left 'weights[currentItem]' columns
                '''
            current_item = total_items - 1

            if (total_items == 0 or max_weight == 0):
                cache[total_items][max_weight] = 0
            elif (weights[current_item] > max_weight):
                cache[total_items][max_weight] = cache[total_items - 1][max_weight]
            else:
                with_item = values[current_item] + \
                    cache[total_items - 1][max_weight -
                                           weights[current_item]]
                without_item = cache[total_items - 1][max_weight]

                cache[total_items][max_weight] = max(
                    with_item, without_item)

    return cache[len(values)][maxWeightConstraint]

import itertools
def knapsack_brute_force(items, capacity):
    all_combos = []
    max_value = -1
    best_combo = None
    for i in range(1, len(items)+1):
        list_of_combos = list(combinations(items, i))
        # Check weight and value
        for combo in list_of_combos:
            value = 0
            weight = 0
            for item in combo:
                value += item.value
                weight += item.weight
            if weight <= capacity:
                 if value > max_value:
                     max_value = value
                     best_combo = combo

    return best_combo

def knapsack_greedy(items, capacity):
    for i in items:
        i.efficiency = i.value / i.weight
    items.sort(keys=lambda x: x.efficiency, reverse=True)

    sack = []
    weight = 0
    for i in items:
        weight += i.weight
        if weight > capacity:
            return sack
        else:
            sack.append(i)

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
