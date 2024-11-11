def largest_of_three(nums):
    if len(nums) < 3:
        raise ValueError("Array must have at least three numbers.")
    
    nums.sort()
    
    # The largest product can be:
    # 1. Product of the three largest numbers
    # 2. Product of the two smallest numbers (negatives) and the largest number
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

# Example usage
nums = [10, -10, 1, 3, 2]
print(largest_of_three(nums))  # Output: 60
