class Solution:

    def subArrayExists(self, arr):

        prefix_sum = 0
        seen = set()

        for num in arr:

            prefix_sum += num

            # Entire prefix sums to 0
            if prefix_sum == 0:
                return True

            # Same prefix sum seen before
            if prefix_sum in seen:
                return True

            seen.add(prefix_sum)


    def subarray_2(self , arr , k):
        seen = set()

        for i in range(len(arr)):
            needed = k - arr[i]
            if needed in seen:
                return True
            
            
            seen.add(arr[i])
    

        return False
    

arr = [1, -2, 1, 0, 5]

print(Solution().subarray_2(arr , k= 0 ))



