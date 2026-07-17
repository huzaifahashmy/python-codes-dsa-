def rod_cutting(price, n):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        max_val = float('-inf')
        
        for j in range(i):
            max_val = max(max_val, price[j] + dp[i - j - 1])
        
        dp[i] = max_val

    return dp[n]


print(rod_cutting([2, 5, 7, 8], 4))




# here the n is the length of the rod and the price array is the price of the rod of length i+1 at index i.


