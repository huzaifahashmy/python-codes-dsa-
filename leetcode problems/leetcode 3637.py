# firstly it has to increase and then decrease and then encrease 

class solution():
    def trionic(self , arr:list[int])-> bool:

        n = len(arr)
        i = 0
        #incereasing part
        while i < n-1 and arr[i] < arr[i+1]:
            i +=1 

        if i == 0:

            return False 
        
        peak = i 

        #decreasing part


        while i < n-1 and arr[i] > arr[i+1]:
            i +=1

        if i == peak:
            return False
        
        valley = i 


        # increasing part

        
        while i < n-1 and arr[i]< arr[i+1]:
            i+=1

        if i == valley:
            return False
        
        return i == n-1 
    


        # increasing part 



sol = solution()

print(sol.trionic([1, 3, 5, 4, 2, 6]))      # True
print(sol.trionic([1, 2, 3, 2, 1, 4, 5]))   # True
print(sol.trionic([1, 2, 3, 4]))            # False
print(sol.trionic([5, 4, 3, 2]))            # False
print(sol.trionic([1, 2, 1]))               # Falt

