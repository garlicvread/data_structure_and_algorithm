import time


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
