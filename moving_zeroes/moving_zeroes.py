'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Check for non-0s
    non_z = [x for x in arr if x is not 0]
    z = [0]*(len(arr)-len(non_z))
    non_z.extend(z)

    return non_z

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
