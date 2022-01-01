def maxSubArray(nums):
    length = len(nums)
    dp_table = [0] * length
    dp_table[0] = nums[0]

    for i in range(1, length):
        dp_table[i]= max(dp_table[i-1] + nums[i], nums[i])
        
    return max(dp_table)
    
    
def main():
    print(maxSubArray([-10, -7, 5, -7, 10, 5, -2, 17, -25, 1]))
    

if __name__ == "__main__":
    main()
    
