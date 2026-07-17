def sum_xor(arr):
    sum = 0 
    
    for i in range(len(arr)):
        for j in range(i+1 , len(arr)):
            sum  += arr[i] ^ arr[j]


    return sum 


print(sum_xor([5, 9, 7, 6]))

