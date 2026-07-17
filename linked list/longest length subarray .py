#User function Template for python3
class Solution:
    # Function to find a continuous sub-array which adds up to a given number.
    def subarray_sum(self, arr, total_sum):
        # Your code here
        
        left = 0
        current_sum = 0

        for right in range(len(arr)):
            current_sum += arr[right]

        # shrink window until valid
            while current_sum > total_sum and left <= right:
                current_sum -= arr[left]
                left += 1

        # check condition
            if current_sum == total_sum and left <= right:
                return [left + 1, right + 1]  # 1-based indexing

        return []
    def prefix_calc(self , arr , key):
        longest_sum = 0

        prefix_sum = 0 
        # prefix_sums = []
        for i in range(len(arr)):
            prefix_sum += arr[i]
            if prefix_sum == key:
                longest_sum = max(longest_sum , i +1 )


        return longest_sum
    

    # def prefix_sum(self , arr):
    #     prefix_sum = 0 
    #     prefix_sums = []
    #     for i in range(len(arr)):
    #         prefix_sum += arr[i]
    #         prefix_sums.append(prefix_sum)

    #     return prefix_sums


    def longest_subarray(self  ,arr , k ):
        prefix_sum = 0 
        longest = 0 
        first_occurence = {0 , -1 }

        # {0 , -1} -> to handle the first case senrio 
        # if the element is found in the first iteration then it will return a positive value

        
        
        for i  , num in enumerate(arr):
            prefix_sum += num
            if prefix_sum - k in first_occurence:
                longest = max(longest , i - first_occurence[prefix_sum - k])

            else:
                first_occurence[prefix_sum]  = i


        return longest
    


        

# print(Solution().prefix_calc([10, 5, 2, 7, 1, -10] , key= 15))

# print(Solution().prefix_calc([-5, 8, -14, 2, 4, 12]  , key= -5))

print(Solution().prefix_sum([10, 5, 2, 7, 1, -10]))


# print(Solution().prefix_sum([-5, 8, -14, 2, 4, 12]))  # the target is k =  -5




        
        



