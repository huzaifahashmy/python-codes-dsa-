class solution():
    def snakeOrder(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        for i in range(m + n - 1):
            if i % 2 == 0:
                for j in range(min(i, m - 1), max(-1, i - n), -1):
                    # so what is this doing ?
                    # it is basically iterating through the diagonal elements of the matrix in a snake-like pattern.
                    # here j is the row index and i-j is the column index.

                    res.append(matrix[j][i - j])
            else:
                for j in range(max(0, i - n + 1), min(i + 1, m)):
                    res.append(matrix[j][i - j])
        return res
    


class solution2():
    def snake(self , arr):
        # now we have to count the number of rows and arrays in the matrix ]\

        if not arr1:
            return 0 
        
        n = len(arr)-1
        m = len(arr[0]) -1
        result = []
        for i in range(len(arr)):
            if i % 2 == 0:
                for j in range(m+1):
                    result.append(arr[i][j])
            else:
                for j in range(m , -1 , -1 ):
                    result.append(arr[i][j])


        return result
    


# len(arr) -> this will return the number of rows in the matrix
# len(arr[0]) -> this will return the number of column of the matrix 
# we eventually have to traverse through the rows only 


arr1 = [[45, 48, 54], [21, 89, 87], [70, 78, 15]]


print(solution2().snake(arr=arr1))

if [45, 48, 54, 87, 89, 21, 70, 78, 15] == solution2().snake(arr1):
    print ("pass")




