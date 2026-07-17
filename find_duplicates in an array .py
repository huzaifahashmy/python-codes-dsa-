class solution():
    def find_duplicates(self ,arr) -> int:
        vistited = [0]*(max(arr) +1)
        for i in range(len(arr)):
            if vistited[arr[i]]:
                return arr[i]
            vistited[arr[i]] = 1

        return -1
    
    



print(solution().find_duplicates([1,3,4,2,2]))
