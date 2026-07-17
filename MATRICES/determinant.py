class solution():
    def determinant(self , mat , n):

        # we also need to call for the base case which in this case is 1 , or 2 

        if n == 1 :
            return mat[0][0]

        if n == 2 :
            return (
                mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
            )        
        det = 0
        for col in range(n):
            submatrix = []

            for row in range(1 , n):
                temp = []

                for c in range(n):
                    if c != col:
                        temp.append(mat[row][c])

                submatrix.append(temp)



            sign = (-1) ** col

            det +=  sign * mat[0][col] * self.determinant(submatrix, n-1 )


        return det 
    


matrix = [
    [2, 1, 3, 4, 5],
    [1, 0, 2, 1, 3],
    [4, 1, 0, 2, 1],
    [3, 2, 1, 0, 4],
    [5, 3, 2, 1, 0]
]

determinant = solution().determinant(mat= matrix, n= 5)


print(determinant )
