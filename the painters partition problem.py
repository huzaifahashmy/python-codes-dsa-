class solution():
    def count_max (self , arr , painters):
        paint = 1
        painters_window = 0
        for i in range(len(arr)):
            if painters_window + arr[i] <= painters:
                painters_window += arr[i]
            else:
                paint+=1 
                painters_window = arr[i]
            
        return paint
    

    def painters(self , arr , k):
        # edge case
        if k > len(arr):
            return max(arr)
        low = max(arr)
        high = sum(arr)
        ans = high
        while low<= high:
            mid = (low + high) // 2
            if self.count_max(arr, mid) <= k:
                ans = mid
                high = mid -1 

            else:
                low = mid + 1 

        return ans


class nigga:
    def search(self, arr, x):
        arr.sort()  # sort first
        
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1
    
class binary_searches():
    def binary_first_last(self , arr , k):
        low = 0 
        high = len(arr) -1
        ans = -1
        while low<=high:
            mid = (low + high)//2
            if arr[mid] == k:
                ans = mid
                high = mid-1
            elif arr[mid] <k:
                low = mid +1 
            else:
                high = mid -1

        # print(ans)

        if ans == -1:
            return [-1 , -1]
        else:
            for i in range(ans ,len(arr)-1):
                if arr[i] != arr[i+1]:
                    return [ans , i]
        


class dihhh:
    def find(self, arr, x):
        low = 0
        high = len(arr) - 1
        ans = -1

        # Find first occurrence
        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == x:
                ans = mid
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        if ans == -1:
            return 0

        # Find last occurrence using your loop idea
        last = ans
        for i in range(ans, len(arr)):
            if arr[i] == x:
                last = i
            else:
                break

        return last - ans +1



    def merge_two_sorted(self,arr1 , arr2):
        index1= 0 
        index2 = 0
        while index1 < len(arr1) and  index2 < len(arr2):
            if arr1[index1] <= arr2[index2]:
                print(arr1[index1])
                index1 +=1 
            else:
                print(arr2[index2])
                index2 +=1

        # we can also pritn put the remainiing arrays as usual 
    # firstly we will print arr1 and then we can print all of the elements of the arr2 
        while index1 < len(arr1):
            print(arr1[index1])
            index1 +=1 
        
        while index2 < len(arr2):
            print(arr2[index2])
            index2 +=1 

    def index_low_mid_high(self , arr , low , mid , high):
        
        arr1 = arr[low:mid+1]
        arr2 = arr[mid+1:high+1]

        print(arr1)
        print(arr2)

        index1= 0 
        index2 = 0
        sorted = []
        while index1 < len(arr1) and  index2 < len(arr2):
            if arr1[index1] <= arr2[index2]:
                sorted.append(arr1[index1])
                index1 +=1 
            else:
                # print(arr2[index2])
                sorted.append(arr2[index2])
                index2 +=1

        # we can also pritn put the remainiing arrays as usual 
    # firstly we will print arr1 and then we can print all of the elements of the arr2 
        while index1 < len(arr1):
            # print(arr1[index1])
            sorted.append(arr1[index1])
            index1 +=1 
        
        while index2 < len(arr2):
            # print(arr2[index2])
            sorted.append(arr2[index2])

            index2 +=1


        return sorted
    

    def merge_sort(self, arr, low, high):
        if low >= high:
            return [arr[low]]   # return single element as list

        mid = (low + high) // 2

        # recursively sort left and right
        left = self.merge_sort(arr, low, mid)
        right = self.merge_sort(arr, mid+1, high)

        # ⚠️ IMPORTANT:
        # your merge function expects original array indices,
        # but here we have new arrays → so we adapt:

        return self.merge_lists(left, right)


    def merge_lists(self, arr1, arr2):
        index1 = 0
        index2 = 0
        merged = []

        while index1 < len(arr1) and index2 < len(arr2):
            if arr1[index1] <= arr2[index2]:
                merged.append(arr1[index1])
                index1 += 1
            else:
                merged.append(arr2[index2])
                index2 += 1

        while index1 < len(arr1):
            merged.append(arr1[index1])
            index1 += 1

        while index2 < len(arr2):
            merged.append(arr2[index2])
            index2 += 1

        return merged


    def remove_duplicates(self, arr):
        if len(arr) == 0:
            return 0

        i = 0
        for j in range(1, len(arr)):
            if arr[j] != arr[i]:
                i += 1
                arr[i] = arr[j]

        return i + 1




# print(dihhh().find([1, 3, 5, 5, 5, 5,5,5, 67, 123, 125] ,5 ))


# print(dihhh().index_low_mid_high([10 , 15 , 20 , 11 , 30]  , 0 , 2 , 4))

# print(dihhh().merge_sort([7,6,5,76,8,9,3,2,4] , 0 , len([7,6,5,76,8,9,3,2,4])-1))

arr = [1,2,2,3,4,4,4]

k = dihhh().remove_duplicates(arr)  #this thing is pretty straight forward and very easy to understansd cuz python modifies the original string while passing into the functions

print(arr[:k])


class search():
    def union(self , arr1 , arr2):
        index1 = 0 
        index2 = 0 
        n = len(arr1) -1 
        m = len(arr2) -1
        sorted = []
        while (index1 < n and index2 < m):
            if arr1[index1] == arr1[index1 +1]:
                index1 +=1 
                continue
            if arr2[index2] == arr2[index2 +1]:
                index2 += 1
                continue
            if arr2[index2] < arr1[index1]:
                sorted.append(arr2[index2])
                index2 +=1 
            elif arr1[index1] < arr2[index2]:
                sorted.append(arr1[index1])
                index1 +=1

            else:
                sorted.append(arr1[index1])
                i +=1 
                j +=1

        while index1 < len(arr1):
            if arr1[index1] == arr1[index1 +1]:
                index1 +=1 
                continue
            sorted.append(arr1[index1])
            index1 += 1

        while index2 < len(arr2):
            if arr2[index2] == arr1[index2 +1]:
                index1 +=1 
                continue
            sorted.append(arr2[index2])
            index2 += 1

        return sorted




class boka:
    def union(self, arr1, arr2):
        i, j = 0, 0
        n, m = len(arr1), len(arr2)
        result = []

        while i < n and j < m:
            if arr1[i] < arr2[j]:
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1

            elif arr2[j] < arr1[i]:
                if not result or result[-1] != arr2[j]:
                    result.append(arr2[j])
                j += 1

            else:
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
                j += 1

        while i < n:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1

        while j < m:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1

        return result
    

    def inversions(self , a):
        i = 0 
        j = 1 
        # i here is a slow pointer
        count = 0 


        while i < len(a):
            if j == len(a ) -1:
                i +=1 
                j = i+1
            elif a[i] > a[j]:
                count+=1
                j+=1 
    

        return count 
    






print(boka().inversions([2 , 4, 1 ,3 ,5]))


# print(search().union(arr1=[3 , 5 , 8] , arr2= [2 , 8,  9 , 10 , 15]))

