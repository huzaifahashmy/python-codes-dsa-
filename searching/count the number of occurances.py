class Solution():
    def countFreq(self, arr, target) -> int:
        low, high = 0, len(arr) - 1
        first = -1

        # find first occurrence
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                first = mid
                high = mid - 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if first == -1:
            return 0

        low, high = 0, len(arr) - 1
        last = -1

        # find last occurrence
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                last = mid
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return last - first + 1


print(Solution().countFreq([10,20,20,20,30], 20))

# the time complexity for this approach is O(logn + target)


