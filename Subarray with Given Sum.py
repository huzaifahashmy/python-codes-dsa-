def find(arr, target_sum):
    prefix_sum = 0
    count = 0
    seen = {0: 1}   # important for subarrays starting at index 0  # basiclly we have seen prefix sum 0 once before we start iterating and also  base case when target sum is 0 and we have prefix sum 0 at the beginning

    for num in arr:
        prefix_sum += num

        # check if needed prefix exists
        if (prefix_sum - target_sum) in seen:
            count += seen[prefix_sum - target_sum]

        # update frequency using if-else
        if prefix_sum in seen:
            seen[prefix_sum] += 1
        else:
            seen[prefix_sum] = 1

    return count

print(find([10, 2, -2, -20, 10], -10))
