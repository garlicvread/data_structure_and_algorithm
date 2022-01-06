"""
When you are given an array of integers that are greater than zero,
find the kth-greatest value from the array.

e.g.) If you are given [2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23] as the input,
          the maximum number: 50
          the second maximum number: 37
          ...
          the smallest number: 1
      As an extended algorithm of the previous one, you need to find the kth greatest number from the array.

Try to find your best solution in minimum time complexity or space complexity.
"""


def kth_max(array, k):
    """
    # Solution 1: Time complexity O(NlogN), space complexity O(N)

    temp_nums = set(array)
    sorted_nums = sorted(temp_nums, reverse=True)
    return sorted_nums[k-1]
    """

    # Solution 2: insertion sort. Time complexity O(N*k^2), space complexity O(1)

    # Exception handling: k cannot be greater than the number of distinct values in the given array.
    ordinal_marker = ('st', 'nd', 'rd')[k-1] if k <= 3 else 'th'

    unique_nums = set(array)

    if len(unique_nums) < k:
        raise IndexError(f"There's no {k}{ordinal_marker} value in the given array.")
    elif k <= 0 or not array:
        raise ValueError("The array must not be an empty array and k should be greater than 0.")

    inf = float('inf')
    memory = [-inf] * k

    # searching for the kth-largest number in the array.
    """
    Multiple for loops are used here to compare 'n' and the values in 'memory'.
    
    When the value of 'memory' is 'm', 'n' must fit the condition of m < n < the next value of m (which is memory[i+1]).
    However, when 'm' is the first value of 'memory', there is no such element as 'memory[i+1]' to compare with.
    In this case, i == 0 is needed to compare with memory[0].
    Without this code, memory[i-1] may return index number -1.
    """
    for n in array:
        if n <= memory[-1]:
            continue

        """
        When there are 'n' and 'm' (the value to be stored to 'n'),
        another for loop is needed to push the original elements to the right.
        The important thing is that the update of value must be done in backward order.
        That is, the value of memory[i+1] must be updated before the value of memory[i].
        
        If the values have been pushed to right after the current m, which is index number i,
        then assign 'n' to i.
        With this process, the current largest value will be updated.

        After completely escaping the loop, the last value in memory is the Kth maximum value.
        So, now we can return the kth largest value.
        """
        for i, m in enumerate(memory):
            if (i == 0 and n > m) or m < n < memory[i-1]:
                for j in range(len(memory)-2, i-1, -1):
                    memory[j+1] = memory[j]
                memory[i] = n
                break

    return memory[-1]


def main():
    print(kth_max([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23], 4))  # should return 34.


if __name__ == "__main__":
    main()
