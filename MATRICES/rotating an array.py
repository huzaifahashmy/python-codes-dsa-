class solution():
    def rotation(self ,arr):
        # first ot transpoe the array
        # new method unlocked !! -> transpose = list(zip(*matrix))
        # transposed_list = [list(row) for row in zip(*matrix)]
        # n = len(arr)
        m = len(arr[0])


        reveersed_list = []
        # transpose  = list(zip(*arr))s
        transposed_list = [list(row) for row in zip(*arr)]
        # now that we have calculated the transpose , we have to reverse each of the submatrices 
        for i in range(m):  # -> this is going to traverse each of the array 
            transposed_list[i].reverse()
            reveersed_list.append(transposed_list[i])

        return reveersed_list
    
    # important insight 
    # reversing rows flips horizontally
    #reversing matrix flips vertically
    
    


arr  = [
    [1,2],
    [3,4], 
    [5,6]
]

print(solution().rotation(arr=arr))





