class solution():
    def update(self , arr):

        n = len(arr)
        m = len(arr[0])
        rows  = set()
        cols = set()

        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    rows.add(i)
                    cols.add(i)


    # now for the second pass -> we will be changing and updating the elements to zero 

        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:   # or because the zero can be present at ay rows or columns 

                    arr[i][j] = 0

        return arr



arr  = [[1,-1,1], [-1,0,1], [1,-1,1]]

print(solution().update(arr= arr))



# so yeah it is easy enough to e digested and to know that it works , i dont know how , but hell nawwww, how the helli it works, it fascinates me the most 



    

