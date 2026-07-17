class solution():
    def equilibrium(self ,arr):
        left_sum = 0 
        rigth_sum = 0

        n = len(arr)

        # just go for the hashing approach
        hash_1 = {}
        hash_2 = {}

        for i in range(n):
            left_sum += arr[i]
            rigth_sum += arr[n -i -1]
            hash_1[i] = left_sum
            hash_2[i] = rigth_sum
        print(hash_1)
        print(hash_2)

        matching = []
        for key in hash_1:
            if hash_1[key] == hash_2[key]:
                matching.append(key)

        return matching[-2]
    
    def approach_2(self, arr):
        total_sum = sum(arr)
        left_sum = 0
        
        result = []
        
        for i in range(len(arr)):
            total_sum -= arr[i]
            
            if left_sum == total_sum:
                result.append(i)
            
            left_sum += arr[i]


        return result

        # now decide what to return
        if len(result) >= 2:
            return result[-2]
        elif len(result) == 1:
            return result[0]   # optional (depends on problem)
        return -1

        


# print(solution().equilibrium([3 , 4, 8 , -9 , 20 , 6]))

print(solution().approach_2([5 , 2 , 2 , 4 , 3 , 4 , 2]))





