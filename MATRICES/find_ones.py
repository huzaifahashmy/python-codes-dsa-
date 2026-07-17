class solution():
    def boolean(self , arr):
        finded_locations_row  = set()
        finded_locations_columns = set()

        n = len(arr)
        m = len(arr[0])

        for i in range(n ):
            for j in range(m):
                if arr[i][j] == 1:
                    finded_locations_row.add(i)
                    finded_locations_columns.add(j)

        for i in range(n):
            for j in range(m):
                if i in finded_locations_row or j in finded_locations_columns:
                    arr[i][j] = 1 
                

        return arr
    
s=lambda m:[[m[r][c]if m[r][c]!='0'else next((d for d in'123456789'if all(d!=m[r][i]!=m[r][c]and d!=m[i][c]!=m[r][c]and d!=m[r//3*3+i//3][c//3*3+i%3]for i in range(9))and not any(s([row[:]for row in m[:r]]+[m[r][:c]+d+m[r][c+1:]]+[row[:]for row in m[r+1:]]))),None)for c in range(9)]for r in range(9)]

arr1 = [[1, 0, 0], [1, 0, 0], [1, 0, 0], [0, 0, 0]]
arr2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 0, 0]]
 
if arr2 == solution().boolean(arr= arr2):
    print("pass")




        

        


        
