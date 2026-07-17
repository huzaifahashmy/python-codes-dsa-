# import bisect 


# arr =  [1,2,3,3,3,3,3,3,4,5,6,7]


# def slice(arr , key) -> int:

#     upperbound = bisect.bisect_left(arr, key)
#     lowerbound = bisect.bisect_right(arr,key)

#     return lowerbound - upperbound


# print (slice(arr=arr ,key= 3))



def occurence(arr, k):

    frequency = {}
    n =len(arr)


    for nums in arr:
        if nums not in frequency:
            frequency[nums] =1 
        else:
            frequency[nums] +=1

    count = 0

    for i in frequency:
        if frequency[i] > n /k:
            count +=1

    return count



class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here

        set_a = set(a)
        set_b = set(b)

        if len(set_a) != len(set_b):
            return False



        for i in set_a:
            if i not in set_b:
                return False
            
        return True 
    
    def first_occuranve(self ,arr):
        frequency = dict()

        for nums in arr:
            if nums not in frequency:
                frequency[nums] = 1

            else:
                frequency[nums] +=1 

        

        for i in range(len(arr)):
            if frequency[arr[i]] > 1:

                return i+1
            
        return -1
    

arr = [1, 2,3,4,5]


print(Solution().first_occuranve(arr=arr  ))


