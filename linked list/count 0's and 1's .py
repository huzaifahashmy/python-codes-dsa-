class Solution:
    def maxLen(self, arr):
        # code here
        count_0 = 0 
        count_1 = 0



        for nums in arr:
            if nums == 0:
                count_0+=1 
            else:
                count_1 +=1


        print(count_0)
        print(count_1)


   


        if count_1 >= count_0:
            return count_0  * 2 
        else:
            return  count_1 * 2 
        

    def prefix_1_0(self, arr):
        
        prefix_sum = [0]*len(arr)

        for i in range(len(arr)):
            if arr[i] == 0:
                prefix_sum[i] = 0
            else:

                prefix_sum[i]  = 1 

        
        # now to calcultate the prefix sum 
        # print(prefix_sum)

        for i in range(1 , len(arr) ):
            prefix_sum[i] = prefix_sum[i] + prefix_sum[i-1]

        
        return prefix_sum 
    

    def ultimate_solution(self , arr):
        prefix_sum = 0 
        max_len = 0
        first_occurence = {0 : -1}
        # in this solution what we have did is that , we have converted all the zeroes to -> -1 
        # and we are running a prefix_sum looop and then comparing the elements which have occured before in their first most occurence



        for i in range(len(arr)):
            if arr[i] == 0:
                prefix_sum += -1 

            else:
                prefix_sum +=  1

            if prefix_sum in first_occurence:
                max_len = max (max_len , i - first_occurence[prefix_sum])

            else:
                first_occurence[prefix_sum] = i

        
        return max_len




# print(Solution().maxLen([1, 0, 1, 1, 1, 0, 0]))

# print(Solution().maxLen([0, 0, 1, 1, 0]))

# arr = [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]


# print(Solution().maxLen(arr= arr))

arr1  = [0, 1, 0, 1, 1, 1, 1]

arr2 = [1, 1, 1, 1, 1, 0, 1]

print(Solution().prefix_1_0(arr=arr1))
print(Solution().prefix_1_0(arr= arr2))


# print(Solution().ultimate_solution(arr= arr))



