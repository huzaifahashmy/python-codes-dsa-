class solution():
    def find(self ,arr, k):
        low = 0 
        high = len(arr) -1
        l = len(arr)
        mid = 0 
        while low <= high:
            mid = (low + high) // 2

            if(arr[mid] > k):
                high =  mid -1

            elif arr[mid] < k:
                low = mid + 1

            else:
                if (mid == l-1) or (arr[mid +1] != arr[mid]):
                    return mid
                else:

                    low  = mid +1 

        return -1 


        
    


print(solution().find([1,2,4,4,5,6] , 4))


# 




                               