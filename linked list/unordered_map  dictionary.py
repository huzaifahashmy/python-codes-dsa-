# unordered map in python is nothing but a dictionary 
# a key and a value pair
# a basic example problem is to find out the distinct elements in the array 

class solution():
    def count_distinct(self , arr):
        # 2st we will try to solve it by dictionary , and then by using set 
        frequency = dict()
        count = 0


        for nums in arr:
            if nums not in frequency:
                frequency[nums] =1 
                count +=1 

            else:
                frequency[nums] +=1 

        out_put = []

        for key , values  in frequency.items():
            out_put.append([key , values])


        return out_put
    
    def count_by_using_set(self ,arr):
        return len(set(arr))
    


    


print(solution().count_distinct([1,1,2,3,4,5,5]))
# print(solution().count_distinct([5,5,5 ,4, 5]))


# expected output -> 3 


