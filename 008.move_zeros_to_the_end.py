"""
An array that has several zeros and positive integers.
Move the zeros to the right end of the array, and keep the order of positive integers steady.
e.g.) Where the inputted array is [0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0],
      then the returned array must be [8, 37, 4, 5, 50, 34, 0, 0, 0, 0, 0, 0].

note: Keep the solution has space-complexity of O(1).
"""


"""
# Solution 1: O(n) time, O(2) space

def moveZerosToEnd(nums):
    temp = []
    zeros = []

    for i in range(len(nums)):
        if nums[i] != 0:
            temp.append(nums[i])
        else:
            zeros.append(nums[i])

    nums = temp + zeros

    return nums
"""

"""
# solution 2: O(n) time, O(1) space

def moveZerosToEnd(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums.pop(i))
    return nums
"""

"""
# solution 3: O(n) time, O(1) space

def moveZerosToEnd(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums[i])
            nums.remove(nums[i])

    return nums
"""


def moveZerosToEnd(nums):
    current_position = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[current_position] = nums[i]
            if i != current_position:
                nums[i] = 0
            current_position += 1

    return nums


def main():
    print(moveZerosToEnd([0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0]))


if __name__ == "__main__":
    main()
