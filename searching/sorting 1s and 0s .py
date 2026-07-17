# def sorting(arr):
#     index_1 = len(arr)-1 
#     inedex_0 = 0 
#     for i in range(0 ,len(arr)):
#         if arr[i] == 0:
#             # arr[index_0] , arr[i] = arr[i] , arr[inedex_0]


#             # arr[inedex_0] = 0 
#             inedex_0 +=1 
#         else:
#             arr[index_1] = 1
#             arr[i] = 0 

#             index_1 -=1

#     return arr
    


# different approach 
def sorting(arr):
    low = 0 
    high = len(arr)-1 

    while low < high:
        if arr[low] == 0:
            low +=1 
        elif arr[high] == 1:
            high -=1 
        else:

            arr[low] , arr[high] = arr[high], arr[low]
            low +=1 
            high -=1 

    return arr 



class Solution:
    def sort012(self, arr):
        # code here
        count_1 = 0 
        count_2 = 0 
        count_0 = 0
        
        for nums in arr:
            if nums == 1:
                count_1 +=1 
            elif nums == 2:
                count_2 +=1 
                
            else:
                count_0 +=1 
                
        return [0]*count_0 + [1]*count_1 + [2]*count_2
    

    def greek_flag(self, arr):
        low = 0 
        mid =  0 
        high = len(arr) -1

        while mid< high:
            if arr[mid] == 0:
                arr[low] , arr[mid] = arr[mid] , arr[low]
                low += 1
                mid +=1
            elif arr[mid] == 1:
                mid +=1 
            else:
                arr[mid], arr[high] = arr[high] , arr[mid]
                high -=1 
            
        return arr
    
    


print(Solution().sort012([1,0,1,0,2,0,2,0,2]))




