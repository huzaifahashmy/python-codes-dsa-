class solution():
    def flip(self, arr):
        for row in arr:
            row.reverse()

        arr.reverse()

        return arr
    

arr = [[1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9]]


print(solution().flip(arr=arr))

