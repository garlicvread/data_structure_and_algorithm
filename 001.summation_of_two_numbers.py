"""
Assume that an array of numbers and a target number are given.
When summation of the two numbers of the given array is the same with the target number, return the two.

1. The array given has no duplicate members.
2. There must be two numbers that are the same as the target number when summed up.

e.g.) Inputted array: [2, 8, 19, 37, 4, 5], target number: 12
      --> return (8, 4) or (4, 8) as the result. The order of returned numbers is not the concern here.
"""


def twoSum(nums, target):
#     # All data in the array 'nums' is scaned. O(n).
#     for n in nums:
    
#         # All data in the array 'nums' is scaned once more. O(n) --> O(n^2).
#         if (target - n) in nums:
#             return n, (target-n)
#     # --> Timeout error occurs.
    
    
    # Sort the inputted array in ascending way.
    nums.sort()
    
    # i: The index number of first number.
    # j: The index number of the last number.
    i = 0
    j = len(nums) - 1
    
    # While i < j, we will compare the summation of nums[i] + nums[j] to the target value.
    while i < j:
    
        # Initiate new parameter 'sum'.
        sum = nums[i] + nums[j]
        
        """
        If the summation of the first and the last member of the inputted array is same to the target value,
        you can return nums[i], the first member and nums[j], the last member.
        """
        if sum == target:
            return nums[i], nums[j]
            
        """
        But the summation of them is bigger than the target value,
        scan the second member from the last of the inputted array
        and calculate the summation of the first member and the newly scanned member,
        which is the second from the last, nums(j-1).
        """    
        elif sum > target:
            j -= 1
            
        """
        If the summation of the two is smaller than the target value,
        the second member from the first of the inputted array
        and calculate the summation of them,
        which is nums[i+1] + nums[j].
        """
        else:
            i += 1


def main():
    print(twoSum([2, 8, 19, 37, 4, 5], 12))


if __name__ == "__main__":
    main()
