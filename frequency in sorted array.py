class solution():
    def frequency(self , arr):
        freq = {}
        for i in range(len(arr)):
            if arr[i] not in freq:
                freq[arr[i]] = 1
            else:
                freq[arr[i]] += 1

        return freq
    
    



print(solution().frequency([1,2,3,4,4,4,5,1,2,3]))

