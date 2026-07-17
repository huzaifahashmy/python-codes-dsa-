class Solution():
    def maxOccured(self, L, R):
        index_array = [0]*max(max(L) , max(R)) + [0]*2

        for i in range(len(L)):
            index_array[L[i]] += 1
            index_array[R[i]+1] -= 1




        # return index_array
        # now we will calculate the prefix sum of the array 
        for i in range(len(index_array)-1):
            index_array[i+1] += index_array[i]

        return index_array.index(max(index_array))


    


print (Solution().maxOccured([1,4,3,1],[15,8,4,9]))

# testing more of them now 

print(Solution().maxOccured([1, 5, 9, 13, 21],[15, 8, 12, 20, 30]))


arr= [1,2,3,4,5,6,7,8,9,10]

print(arr.index(max(arr)))












        