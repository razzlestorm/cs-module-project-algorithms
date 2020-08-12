'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # check for negatives and 0
    methods = [3, 2, 1]
    if n <= 0:
        return 0

    else:
        for m in methods:
            # Making sure number is greater than cookie-eating methods
            if n - m < 0:
                continue
            else:
                for num in methods:

        # Create a set that will store each solution (helps with duplicates),

        # check what combination of steps can = n


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
