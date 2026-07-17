class solution:
    def left_rotate(self, arr, d):
        n = len(arr)
        d = d % n  # Handle cases where d >= n\


        # so the idea is to take the first d elements and move them to the end of the array, while keeping the rest of the elements in their original order. We can achieve this by slicing the array into two parts: the first d elements and the remaining elements. Then we concatenate these two parts in reverse order.
        return arr[d:] + arr[:d]    
    

    


print(solution().left_rotate([1, 2, 3, 4, 5], 2))  # Output: [3, 4, 5, 1, 2]


