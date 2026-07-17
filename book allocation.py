from typing import List

class Solution:
    def canAllocate(self, books: List[int], M: int, cap: int) -> bool:
        """Can we split books into <= M contiguous groups, each with sum <= cap?"""
        students = 1
        curr = 0  # current student's window sum

        for pages in books:
            if pages > cap:          # single book exceeds cap — impossible
                return False

            if curr + pages > cap:   # close current window, open a new one
                students += 1
                curr = pages
                if students > M:
                    return False
            else:
                curr += pages        # extend current window

        return True

    def findPages(self, books: List[int], N: int, M: int) -> int:
        if M > N:
            return -1

        low  = max(books)            # lower bound: biggest single book
        high = sum(books)            # upper bound: one student reads all
        ans  = high

        while low <= high:
            mid = (low + high) // 2

            if self.canAllocate(books, M, mid):
                ans = mid
                high = mid - 1       # try to minimize further
            else:
                low = mid + 1        # need larger cap

        return ans
    


class baklol():
    def can_allocate(arr , pages):
        stu = 1
        pages_student = 0 
        for i in range(len(arr)):
            if pages_student + arr[i] <= pages:
                pages_student += arr[i]
            else:
                stu +=1
                pages_student = arr[i]

        return stu

    def binary(self , arr , n):
        if n > len(arr):
            return -1
        
        low = max(arr)
        high = sum(arr)
        ans = high

        while low <= high:
            mid = (low + high ) // 2
            if (n == self.can_allocate(arr , mid)):
                ans = mid
                high = mid -1
            else:
                low = mid +1

        return ans 
    
    


                





# --- quick test ---
if __name__ == "__main__":
    sol = Solution()

    print(sol.findPages([12, 34, 67, 90], 4, 2))   # 113
    print(sol.findPages([10, 20, 30, 40], 4, 2))   # 60
    print(sol.findPages([15, 17, 20], 3, 5))       # -1  (M > N)
    print(sol.findPages([25], 1, 1))               # 25
    print(sol.findPages([5, 5, 5, 5], 4, 4))       # 5