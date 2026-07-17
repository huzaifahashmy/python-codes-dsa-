def soring_two(arr1 , arr2):
    i = len(arr1) -1    # ending element of the array 1
    j = 0   # starting element of the array 2 
    # for x in range(len(arr2)):
    #     if arr2[j] < arr1[i]:
    #         arr1[i] , arr2 [j] = arr2[j] , arr1[i] # swapping the elements 
    #         j +=1 
    #         i -=1

    while i >=0 and j <len(arr2):

        if arr2[j] < arr1[i]:

            arr1[i] , arr2 [j] = arr2[j] , arr1[i] # swapping the elements 
            j +=1 
            i -=1
        
        else:   # break its beacuase of one simple logic (both of the arrays are sorted now)
            break 

                
        
    return sorted(arr1) , sorted(arr2)


# [2, 4, 7, 10], b[] = [2, 3] 

print(soring_two([2,4,7,10] , [2,3]))


