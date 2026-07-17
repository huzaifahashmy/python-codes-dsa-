class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            
            self.quickSort(arr, low, p - 1)
            self.quickSort(arr, p + 1, high)

        return arr

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
        
        
# so this algorithm is a very beautiful algorithm which shows ow beautiful and how remarkable a sorting algorithm can be 

arr = [6,5,8,9,3,5,7,8,2,4,6,1]
print(Solution().quickSort(arr , 0 , len(arr)-1 ))




