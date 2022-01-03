"""
A list of integers that are greater than 0.
The list given is sorted in ascending manner and includes random duplicate numbers.
Remove duplicate number from the list then print it.

e.g.) Where the inputted list is [1, 1, 2, 2, 2, 2, 5, 7, 7, 8],
      then the returned list must be [1, 2, 5, 7, 8].
"""


def removeDuplicate(nums):
    # return list(set(nums))
    result = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            # print("nums[i]: ", nums[i], ",", "nums[i-1]: ", nums[i-1])
            result.append(nums[i])

    return result


def main():
    print(removeDuplicate([1, 1, 2, 2, 2, 2, 5, 7, 7, 8]))


if __name__ == "__main__":
    main()
