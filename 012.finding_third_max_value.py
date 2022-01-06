"""
When you are given an array of integers that are greater than zero,
find the third-greatest value from the array.

e.g.) If you are given [2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23] as the input,
          the maximum number: 50
          the second maximum number: 37
          the third maximum number: 34
      Thus, the return must be 34.

Try to find your best solution in minimum time complexity or space complexity.
"""


def thirdMax(nums):
    """
    Solution 1: Time O(NlogN) and Space O(1)

    if len(nums) < 3:
        return False
    else:
        nums.sort()
        return nums[-3]
    """


    # Solution 2: Time O(N) and Space O(1)

    # Set the first to third number to be the negative infinity
    first = -float('inf')
    second = -float('inf')
    third = -float('inf')

    for num in nums:

        # If the parameter 'num' is greater than the first number, refresh all three numbers.
        if num > first:
            third = second
            second = first
            first = num

        # If the parameter 'num' is in between the first number and the second number,
        # refresh the second and the third numbers.
        elif second < num < first:
            third = second
            second = num

        # If the parameter 'num' is in between the second number and the third number,
        # refresh the third number only.
        elif third < num < second:
            third = num
    return third


def main():
    print(thirdMax([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23]))  # should return 34.


if __name__ == "__main__":
    main()
