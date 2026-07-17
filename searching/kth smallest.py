class solution():
        def partition(self, arr, low, high):

            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1
        
        def find_kth(self , arr , k):
            
            low = 0
            high = len(arr)-1 
            while(low <= high):
                
                p = self.partition(arr=arr ,low=low , high= high)

                if p == k-1:
                     
                    return arr[p]
                elif p > k-1:
                    high = p-1
                else: 
                    low = p+1
            return -1 
        


# we also have implemented a binary  search approach for  this function 



print(solution().find_kth([9,8,7,6,5,4,3,2,1], 8))

        