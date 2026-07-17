class solution():
    def finding(self , arr)-> int:
        count = 0

        max_1= 0
        res = 0 
        for i in range(len(arr)-1):
            
            if arr[i] == 0:
                count = 0 
            else:
                count +=1
                res = max(res , count)
                

        return res
    

print(solution().finding([0,1,0,1,0,1,1,1,0,1,1]))  # Output: 3








