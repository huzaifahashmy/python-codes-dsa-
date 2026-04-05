



def matches(arr1 , arr2 , target):
    
    if (len(arr1) >= len(arr2)):
        for i in arr1:
            flag = 0
            for j in arr2:
                if i+j == target:
                    print([i , j])
                    flag = 1
            if flag == 1:
                continue


    elif(len (arr1) < len(arr2)):
        for i in arr2:
            flag = 0 
            for j in arr1:
                if i+j == target:
                    flag = 1 

                    print([i , j])
            if flag == 1:
                continue


    else:
        return 0 
    
    
arr1 = [1, -2, 4, -6, 5, 7]
arr2 = [6, 3, 4, 0]


target  = 8 

def optimal_matches(arr1 , arr2 , target):
    freq = {}
    for num in arr2:
        freq[num] = freq.get(num , 0) + 1

    results = []

    for i in arr1:
        j = target - i    
        if j in freq:
            for _ in range(freq[i]):
                results.append([i,j])

    results.sort()
    return results


 

matches(arr1 , arr2 , target)



print("hhowryyy")