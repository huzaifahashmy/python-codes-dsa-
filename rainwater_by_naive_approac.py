def maxWater(arr):
    res = 0

    # For every element of the array
    for i in range(1, len(arr) - 1):

        # Find the maximum element on its left
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        # Find the maximum element on its right
        right = arr[i]
        for j in range(i + 1, len(arr)):
            right = max(right, arr[j])

        # Update the maximum water
        res += (min(left, right) - arr[i])

    return res
# so basically we are finding largest elelemtn on its left and righr for every element in the list

# and then finding the reseviour value by substracting the min of the left or right value 
if __name__ == "__main__":
    arr = [2, 1, 5, 3, 1, 0, 4]
    print(maxWater(arr))