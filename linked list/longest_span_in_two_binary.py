class solution():
    def equal_sum(self , arr1, arr2):
        diff = [a - b for a , b in zip(arr1 , arr2)]

        prefix_sum = 0 
        longest = 0 
        first_occurence = {0 : -1}

        for i , num in enumerate(diff):
            prefix_sum +=num 

            if prefix_sum in first_occurence:
                longest = max(longest , i - first_occurence[prefix_sum])

            else:
                first_occurence[prefix_sum]  = i
            
        return longest 
    



arr1 =[0, 1, 0, 1, 1, 1, 1]

arr2 = [1, 1, 1, 1, 1, 0, 1]
print(solution().equal_sum(arr1=arr1 , arr2= arr2))




        