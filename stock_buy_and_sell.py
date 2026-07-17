arr1 = [1, 3, 6, 9, 11]



def max_profit(arr):
    profits = []
    max_profit = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            max_profit += arr[i+1] - arr[i]
        else:
            profits.append(max_profit)
            max_profit = 0 
    
    profits.append(max_profit)
    if len(profits) == 0:
        return 0 
    else:
        print(profits)
        return max(profits)
    
print(max_profit(arr1))

