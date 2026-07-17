def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])  # Compare current element with the sum of current element and previous sum
        max_sum = max(max_sum, current_sum)   # Update max_sum if current_sum is greater

    return max_sum

def min_subarray(nums):
    current_sum = nums[0]
    min_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = min(nums[i], current_sum + nums[i])  # Compare current element with the sum of current element and previous sum
        min_sum = min(min_sum, current_sum)   # Update min_sum if current_sum is smaller

    return min_sum

def max_circular_subarray(nums):
    max_sum = max_subarray(nums)
    min_sum = min_subarray(nums)

    # If all numbers are negative, return the maximum sum found by max_subarray
    if max_sum < 0:
        return max_sum

    # Otherwise, return the maximum of max_sum and the sum of the array minus min_sum
    return max(max_sum, sum(nums) - min_sum)
# Example usage:
nums = [5, -3, 5]
print(max_circular_subarray(nums))  # Output: 10 (5 + 5)

nums = [-2, -3, -1]
print(max_circular_subarray(nums))  # Output: -1 (the maximum subarray

