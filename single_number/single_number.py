from collections import Counter
'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    checker = []
    for ii in arr:
        if ii not in checker:
            checker.append(ii)
        else:
            checker.remove(ii)
    return checker[0]
    #return [num for num in Counter(arr) if Counter(arr)[num] < 2][0]



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
