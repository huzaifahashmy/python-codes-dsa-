class solution():
        
        def binary_search(self, arr, low, high, key):

            while low <= high:

                mid = (low + high) // 2

                # element found
                if arr[mid] == key:
                    return mid  

                # search right half
                elif key > arr[mid]:
                    low = mid + 1

                # search left half
                else:
                    high = mid - 1

            # element not found
            return -1
    

        def binary(self , arr , key):
            n = len(arr)
            m = len(arr[0])
            low = 0 
            high  = 0 

            for i in range(n):
                low =  0# arr[i][0] ! only the index element only
                high =  m -1 # arr[i][m-1]

                if arr[i][low] <= key and arr[i ][high] >= key:
                    mid = self.binary_search(arr[i] , low= low  , high= high , key=key)
                    if mid == -1:
                        continue
                    else:
                        return [i , mid]




# the time complexity of this approach is also optimal but we have a better approach 
# n log(m)  ->  O(n + m )
# simple sudo code 
# start from the rightmost element and increase and decrease accordingly 
# if key > current -> move down 
# if key < current -> move up 
# untill the key is found or we are out of bounds
# to check weather the element is in between the (0,0) <-> (n,m)
        def optimal(self , arr , key):
            n = len(arr) -1

            m = len(arr[0]) -1
            right =  m     # -> column
            left = 0   # -> row
            if not (arr[0][0] <= key and arr[n][m]  >= key):
                return 0 


            while left <= n  and right >= 0:
                
                if arr[left][right] == key:

                    return 1 
            
                elif arr[left][right] > key:
                    right -=1 
                else:
                    left +=1 

            return 0 
        
            

print(solution().optimal(arr=[[3, 30, 38],[20, 52, 54],[35, 60, 69]] , key= 20))







                    
