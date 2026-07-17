def prod(arr):

    res = [0]*len(arr)
    prod_without_zero  = 1

    prod_with_zero = 0


    for i in range(len(arr)):
        if arr[i] != 0:

            prod_without_zero *= arr[i]

    if arr.count(0)>=2:
        return list([0 for _ in range(len(arr))])

    if 0 in arr:
        # we almost forgot of the base test case for our array 
        # like what if if our array has more than two 0oes  huhh 
        for i in range(len(res)):
            if arr[i] == 0:
                res[i] = prod_without_zero
            else:
                res[i] = prod_with_zero
    else:
        for i in range(len(arr)):
            res[i] = prod_without_zero/arr[i]


    return list(map(int, res))





print(prod([12 , 0 , 0]))


        

