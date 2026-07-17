class Solution:
    def merge(self, arr, low, mid, high):
        left = low
        right = mid + 1
        temp = []
        count = 0

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                count += (mid - left + 1)
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        return count

    def mergeSort(self, arr, low, high):
        # if low >= high 
        count = 0
        if low >= high:
            return count
        
        if low < high:
            mid = (low + high) // 2
            count += self.mergeSort(arr, low, mid)       # we all have to add the remianing counts to the main count in ach recursion
            count += self.mergeSort(arr, mid + 1, high)  #same applies here as well
            count += self.merge(arr, low, mid, high)     # finally it adds up
        return count

    def inversionCount(self, arr):
        return self.mergeSort(arr, 0, len(arr) - 1)
    

class Solution:
    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            # swap
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


    def partition(self , arr , p):
        low = 0 
        high = len(arr)-1 

        temp = []
        while p >= arr[low]:
            temp.append(arr[low])
            low +=1 

        # now to add the remaining elements 
        temp[low] = p

        while low <= high:
            temp.append(arr[low])
            low +=1 


        return temp


    def optimised_partition(self , arr , p):
        left = []
        right = []
        for nums in arr:
            if nums < p:
                left.append(nums)
            elif nums > p:
                right.append(nums)

        return left + [p] + right
    

    def pivot_highly_optimised(self , arr ,low , high ):
        pivot = arr[high]
        # h = len(arr) - 1
        i =  low -1 
        for j  in range(low , high):
            if (arr[j] < pivot):
                i +=1 
                arr[i] , arr[j] = arr[j] , arr[i] 

        # arr[ i +1 ] = pivot
        # so rather tahn declaring the elements , we wil just swap it up 

        arr[i+1] , arr[high] = arr[high] , arr[i+1]

        return i+1
    
    def qsort(self , arr , low , high):
        if low < high:
            p = self.pivot_highly_optimised(arr,low ,high)
            self.qsort(arr , low , p-1)
            self.qsort(arr, p+1 , high)


        return arr
    

arr = [1,2,3,4,5,6,7,23,45,24,8]



print(Solution().qsort([1,2,3,4,5,6,7,23,45,24,8] , low= 0 , high= len(arr)-1))






