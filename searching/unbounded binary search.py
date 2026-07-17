class Solution:
    def unboundedBinarySearch(self, arr, target):
        low = 0
        high = 1

        # Expand the range exponentially
        while high < len(arr) and arr[high] < target:
            low = high
            high = high * 2
            
        high = min(high, len(arr) - 1)

        # Binary Search
        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
    


print(Solution().unboundedBinarySearch(list(range(1 , 1000000)), 245369))