class Solution():
    def balanceSums(self ,mat):
        n = len(mat) 

        sum_row = [0] * n
        sum_column = [0]*n

        for i in range(n):
            for j in range(n):
                sum_row[i] += mat [i][j]
                sum_column[j] += mat[i][j]

        target = max(max(sum_column) , max (sum_row))

        operations = 0

        for i in range (n ):
            operations += (target - sum_row[i])

            
        return operations
    

arr = [[1, 2, 3],
                [4, 2, 3],
                [3, 2, 1]]


print (Solution().balanceSums(mat= arr))

