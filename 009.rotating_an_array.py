"""
An array that includes positive integers and an integer 'k' are given.
Rotate the array given as much as 'k'.

e.g.) Where the inputted array is [1, 2, 3, 4, 5, 6, 7, 8, 9] and the given number is 4,
      the returned array must be [6, 7, 8, 9, 1, 2, 3, 4, 5].

note:
    1. k < length of the given array.
    2. Make the code has O(1) space complexity. You can use the given function "partialReverse()".
"""


def rotateArray(nums, k):
    """
    This code does not work properly.
    The calculated result through this code is [6, 7, 8, 9, 1, 2, 3, 4, 5], and this fits the condition.
    However, when k=0, the result is [2, 3, 4, 5, 6, 7, 8, 9, 1]
    In this case, the result must be identical to the original array.

    # The code below is not working properly.

    for i in range(k+1):
    nums.append(nums.pop(0))
    """

    idx = len(nums) - k
    nums = nums[idx:] + nums[:idx]

    return nums


def partialReverse(nums, start, end):
    for i in range(0, int((end - start) / 2) + 1):
        temp = nums[start + i]
        nums[start + i] = nums[end - i]
        nums[end - i] = temp


def main():
    nums = [1, 2, 3, 4, 5]
    partialReverse(nums, 1, 3)  # returns [1, 4, 3, 2, 5]
    print(nums)
    print(rotateArray([1, 2, 3, 4, 5, 6, 7, 8, 9], 0))  # must return [6, 7, 8, 9, 1, 2, 3, 4, 5].


if __name__ == "__main__":
    main()
