class solution():
    def __init__(self):
        print("solving the two sum problem")
        return
    
    def two_sum(self , arr , key):
        seen = set()
        for nums in arr:
            adding = key-nums

            # seen.add(adding)
            if adding in seen:
                return True
            
            seen.add(adding)
        return False
    
    def subset_atleast_zero(self  , arr):
        # the key implementation over here is to imlement prefix sum 
        # and to create a set for that prefix 
        # the key logic over here is that, if one of the prefix sums repeats itself , then it is TRUE
        
   
        prefix_set = set()
        prefix_sum = 0

        for num in arr:
            prefix_sum +=num

            if prefix_sum == 0:
                return True

            if prefix_sum in prefix_set:
                return True 
            
            prefix_set.add(prefix_sum)

        return False 
    


    





    

arr = [1, 4, 6, 0]
target = 8

# print(solution().two_sum(arr=arr , key= target))

print(solution().subset_atleast_zero(arr= [1, 2, -1]))
