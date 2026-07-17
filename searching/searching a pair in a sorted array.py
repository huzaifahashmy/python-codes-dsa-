class solution():
    def search(self , array , k):
        j = len(array) -1
        count = 0 

        for i in range(len(array)):
            if array[i] + array[j] == k:
                count += 1
                j = j-1 
                
            
            elif array[i] + array[j] > k:

                # so here what we are trying to achieve is pretty straightforward in the code
                #as here we are trying to find a pain in a sorted array 
                # so here the basic terminologies changes 

                j = j-1 
            else:
                i = i+1

        return count
    
    


print(solution().search([1, 1, 1, 1], 2))




