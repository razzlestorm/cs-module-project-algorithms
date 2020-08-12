#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # Your code here
    # keep track of each combination
    # check for stop condition
    if amount < 0:
        return []
    elif amount == 0:
        return [[]]
    combinations = []

    # iterate through coins, checking largest first
    for used_coin in sorted(denominations)[::-1]:
        # each time a coin is used, subtract it from amount
        combination = making_change(amount - used_coin, denominations)
        for combo in combination:
            combo.append(used_coin)
            combinations.append(combo)
    return combinations


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
