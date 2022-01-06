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

    # Solution 2: insertion sort. Time complexity O(N^2), space complexity O(1)

    # Exception handling: k cannot be greater than the number of distinct values in the given array.
    ordinal_marker = ('st', 'nd', 'rd')[k-1] if k <= 3 else 'th'

    unique_nums = set(array)

    if len(unique_nums) < k:
        raise IndexError(f"There's no {K}{ordinal_marker} value in the given array.")
    elif k <= 0 or not array:
        raise ValueError("The array must not be an empty array and k should be greater than 0.")

    inf = float('inf')
    memory = [-inf] * k

    # searching for the kth-largest number in the array.
    for n in array:
        if n <= memory[-1]:
            continue

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
