#!/usr/bin/python

import sys

# dynamic programming
def rock_paper_scissors(n):
    # list we will be pulling from
    iters = ['rock', 'paper', 'scissors']
    # create the entire base array we will be using
    output = [[] for _ in range(3**n)]
    # This is the number of times each iter choice will appear at the base of the tree
    while n > 1:
        base_times = 3**(n-1)
        # iterating over entire array and appending the base
        for jj in range(0, len(output)):
            output[jj].append(iters[jj//base_times])
        n -= 1
    for ii in range(0, len(output)):
        output[ii].append(iters[ii%3])
    print(output)
    return output


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
