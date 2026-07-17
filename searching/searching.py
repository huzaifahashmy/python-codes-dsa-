class Solution():
    def search(self , arr , key):
        low = 0 
        high = len(arr) -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == key:
                return mid

            # left half sorted
            if arr[low] <= arr[mid]:
                if key >= arr[low] and key < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1 

            # right half sorted
            else:
                if key > arr[mid] and key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
    
    


print(Solution().search([5, 6, 7, 8, 9, 10, 1, 2, 3], 2))