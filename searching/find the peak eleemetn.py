class solution():
    def peak(self , arr):
        low = 0 
        high = len(arr) -1
        while low <= high:
            mid = (low+high) //2

            if ((mid == 0 or arr[mid -1] <= arr[mid]) and (mid == len(arr)-1 or arr[mid+1] <= arr[mid])):
                return arr[mid] 
            
            if mid > 0 and arr[mid -1] >= arr[mid]:
                high = mid -1 

            else:
                low = mid +1

        return -1 

    def mylogic(self , arr):
        if len(arr) > 0:

            return True
        
        return False
    


print(solution().mylogic([]))


