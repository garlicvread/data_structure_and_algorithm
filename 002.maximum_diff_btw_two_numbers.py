"""
Assume that an array of integers of bigger than zero.
Write the code that returns the maximum value of difference between two numbers.

e.g.) Input: [2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23]
      Output: 49 (∵ 49 = 50-1, '50' is the biggest member and '1' is the smallest member.)

Note
1. Return a positive number, so not -49, but 49 must be returned in case of given example above.
2. The size of array is greater or the same with 2.
"""


import time  # To check how much time is needed to execute the code.


def maxTwoDiff(nums):
    # The simplest way and this returns correct answer.
    a = max(nums)
    b = min(nums)
    return abs(a-b)

    # # Slightly unefficient code.
    # nums.sort()
    # return nums[-1] - nums[0]  # nums[-1] is the same with nums[len(nums) - 1]


def main():
    # start = time.time()
    print(maxTwoDiff([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23]))
    # end = time.time()
    # print('Time: ', end - start)


if __name__ == "__main__":
    main()
