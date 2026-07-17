# obvious cases -> to print all of the first and last row 
# but the last row -> we only have to print the row in reverse 
# first_row
# last_rev
# first , last ,

# to be appended in this manner first_row + last + last_rev + first


# class solution():
#     def boundry(self , arr):
#         first_row = []
#         last_row = []
#         first = []
#         last = []
#         final = []
        

# arr = [[1,2 ,3 ],[4 , 5,6] , [7 , 8, 9]]

# print(arr[0]) # -> this will return the first matrix 


# jsut traverse through the whole array niqqa 
# result = []
# n = len(arr)
# m = len(arr[0])
# for i in range(n):
#     for j in range(m):
#         if i == 0 or (i == m-1 ) or j == 0 or j == n-1:

#             result .append(arr[i][j])




class solution():
    def boundry(self , arr):
        
        n = len(arr)       # rows
        m = len(arr[0])    # cols
        result = []

        # Top row
        for j in range(m):
            result.append(arr[0][j])

        # Right column
        for i in range(1, n):
            result.append(arr[i][m-1])

        # Bottom row
        for j in range(m-2, -1, -1):
            result.append(arr[n-1][j])

        # Left column
        for i in range(n-2, 0, -1):
            result.append(arr[i][0])

        return result
    

    def transpose(self , arr):
        n = len(arr)
        m = len(arr[0])
        # trans = [[0]* n]* m # this line of code has some seroiuos problems in it  -> sp use list comprehesnsion 
        trans = [[0 for _ in range(n)]for _ in range(m)]
        print(trans) # no. of rows have now become no. of colums and vice - versa
        print(arr)
        for i in range(m):
            for j in range(n):
                trans[i][j] = arr[j][i]


        return trans
    


                

        # return trans
        # for i in range(n):
        #     for j in range(m):
        #         trans.append(arr[j][i])
        # return trans 


    

arr = [
    [1, 2, 3],
    [4, 5, 6]
]

print(solution() . transpose(arr=arr))

    


