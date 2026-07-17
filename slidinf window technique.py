class solution():
    def slidinf(self ,arr , k):\
        # let us evaluate the sum for the first k elements 
        max_sum = 0


        window_sum = sum(arr[:k])
        max_sum = window_sum



        for i in range(k , len(arr)):
            window_sum += arr[i]  # add the next 
            window_sum -= arr[i-k]  # remove the previous 

            max_sum  = max(window_sum, max_sum)

        return max_sum



print(solution().slidinf([1 , 8 , 30 , -5 , 20 , 7] , 3))







            

            