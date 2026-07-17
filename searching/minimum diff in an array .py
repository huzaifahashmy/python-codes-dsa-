class solution():
    def minimum_diff(self , arr):
        first_min = arr[0]
        last_min = arr[0]
        for i in range(len(arr)-1):
            if arr[i] < first_min:
                first_min = arr[i]

        for i in range(len(arr)-1):
            if arr[i] < last_min: 
                last_min = arr[i]



arr = [7, 2, 10, 4, 3]

# first = float('inf')
# second = float('inf')

# for num in arr:
#     if num < first:
#         second = first
#         first = num
#     elif first < num < second:
#         second = num

# if second == float('inf'):
#     print("No second minimum")
# else:
#     print(second , first)



class sol():
    def second(self ,arr):
        first = float('inf')
        second = float('inf')
        for num in arr:
            if num < first:
                second = first
                first = num

            if first < num < second :
                second = num 

        if num == float('inf'):
            return 0
        
        else:
            return second - first
        
    def optimal_approach(self, arr):
        arr.sort()
        min_diff = float('inf')
        for i in range(1 , len(arr)):
            min_diff = min(min_diff , arr[i] - arr[i-1])
            #most efficiant appraoach so faar 
            #first sort the array and then find the min diff while traversing through the array


        return min_diff
    



        


# print(sol().second([1,3,4,5]))
print(sol().optimal_approach([1,3,4,5]))









            
