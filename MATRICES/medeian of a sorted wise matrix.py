from bisect import bisect_right

class Solution:

    def median(self, matrix, r, c):

        # find minimum element
        low = min(row[0] for row in matrix)

        # find maximum element
        high = max(row[-1] for row in matrix)

        # required position of median
        desired = (r * c) // 2

        while low < high:

            mid = (low + high) // 2

            # count elements <= mid
            count = 0

            for row in matrix:
                count += bisect_right(row, mid)

            # move right
            if count <= desired:
                low = mid + 1

            # move left
            else:
                high = mid

            # well that's how we do it right ?
            # middle element is taken out by dividing the low and high by 2 
            

        return low