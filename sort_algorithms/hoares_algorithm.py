class Solution:
    def hoares(self, arr, low, high):
        pivot = arr[low]
        i = low - 1
        j = high + 1

        while True:
            i += 1
            while arr[i] < pivot:
                i += 1

            j -= 1
            while arr[j] > pivot:
                j -= 1

            if i >= j:
                return j

            arr[i], arr[j] = arr[j], arr[i]

    def quicksort(self, arr, low=0, high=None):
        if high is None:
            high = len(arr) - 1

        if low < high:
            p = self.hoares(arr, low, high)
            self.quicksort(arr, low, p)       # important: includes p
            self.quicksort(arr, p + 1, high)

        return arr
    


arr = [2,34,6,876,56,33,3,45,67,7,8,56,323]




print(Solution().quicksort(arr=arr))
