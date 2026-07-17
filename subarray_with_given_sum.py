class solution():
    def subarray(self, arr , k):

        first_index = 0 
        sum = 0

        for i in range(len(arr)):
            sum += arr[i]

            if sum == k:
                return(first_index +1  , i +1)
            elif sum > k:
                sum -= arr[first_index]
                first_index += 1


        return []

print(solution().subarray([5, 3, 8, 10] , 8))




    