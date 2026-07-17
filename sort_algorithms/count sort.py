class solution():
    def count_sort(self , arr):
        n = len(arr)
        count = [0]*n
        for i in range(n):
            count[arr[i]] += 1 

        # now to append those element back to the array itself
        index = 0

        for i in range(len(count)):

            for j in range(count[i]):
                arr[index] = i
                index +=1 
        

        print(arr)

    


solution().count_sort([5,4,4,3,2,1])

# maaan this counting sort really rocks



