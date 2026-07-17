class solution():
    def triplet(self , arr , x):
        n = len(arr)
        arr.sort()
        # first approach is to implement the 2 pointer method
        for i in range(n-2):
            left = i+1 
            right = n-1
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                if current_sum == x:
                    return True 
                
                elif current_sum < x:
                    left +=1 
                else:
                    right -=1 

        return False
    

        

print(solution().triplet([1, 4, 45, 6, 10, 8] , 13))
