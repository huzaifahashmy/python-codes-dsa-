class solution():
    def calculation(self , arr , tar):
        count = 0 
        prefix_sum = 0

        freq = {0 : 1}

        for nums in arr:
            prefix_sum += nums

            if prefix_sum - tar in freq:

                count += freq[prefix_sum - tar]

            freq[prefix_sum] = freq.get(prefix_sum , 0 ) +1

        return count
    


arr = [10, 2, -2, -20, 10] 
tar = -10

print(solution().calculation(arr= arr , tar= tar))

