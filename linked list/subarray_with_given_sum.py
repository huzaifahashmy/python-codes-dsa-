#User function Template for python3
class Solution:
    # Function to find a continuous sub-array which adds up to a given number.
    def subarray_sum(self, arr, total_sum):
        # Your code here
        left  = 0 
        curr_sum  = 0 
        for right in range(len(arr)):
            curr_sum += arr[right]

            while curr_sum > total_sum:
                curr_sum -= arr[left]

                left +=1 

            if curr_sum == total_sum:

                return[left +1  , right +1]


            
