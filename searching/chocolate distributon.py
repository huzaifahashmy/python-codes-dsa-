class slolution():
    # def check_min_max_subarrray(self , arr):

    def chocolate(self  , arr , m):
        arr.sort()
        # new_arr = arr[:m]
        # print(new_arr)
        starting = 0 
        lasting = m
        minimum = float('inf')
        maximum = float('-inf')
        min_diff = float('inf')
        for i in range(len(arr)-m):
            # minimum = min(minimum , min(arr[starting : lasting]))
            # maximum = max(maximum , max(arr[starting : lasting]))
            diff = max(arr[starting : lasting]) - min(arr[starting:lasting])

            starting +=1 
            lasting +=1
            
            min_diff = min(min_diff , diff)
            print(min_diff)



        
        return min_diff
    

print(slolution().chocolate([3, 4, 1, 9, 56, 7, 9, 12] , 5))

