'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    list_of_ints = []
    left_edge = 0
    right_edge = k
    # use slicing to view elements:
    while right_edge <= len(nums):
        max_val = max(nums[left_edge:right_edge])
        list_of_ints.append(max_val)
        left_edge += 1
        right_edge += 1
    return list_of_ints


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
