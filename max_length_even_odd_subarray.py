class solution():
    # def max_even_odd(self ,arr)->int:
    #     count  = 0 
    #     res = 0 

    #     if len(arr) == 1:
    #         return 1
    #     elif not arr:
    #         return 0
    #     for i in range(len(arr)-1):
    #         if (arr[i]*arr[i+1]) %2 ==0:

    #             if arr[i] %2 != 0 or arr[i+1] %2 !=0:
    #                 count +=1
    #                 res = max(count , res)

    #             else:
    #                 count = 0 

    #     if res == 0:
    #         return 0 
    #     else:
    #         return res +1
    

    def max_even_odd(self, arr) -> int:
        if not arr:
            return 0

        res = 1
        curr = 1

        for i in range(1, len(arr)):
            if arr[i] % 2 != arr[i-1] % 2:
                curr += 1
                res = max(res, curr)
            else:
                curr = 1

        return res


print(solution().max_even_odd([10,12,14,7,8]))        # Expected: 3
print(solution().max_even_odd([1,2,3,4,5]))           # Expected: 5
print(solution().max_even_odd([2,4,6,8]))             # Expected: 1
print(solution().max_even_odd([1,3,5,7]))             # Expected: 1
print(solution().max_even_odd([2,4,1,3,6,5,8]))       # Expected: 5
print(solution().max_even_odd([7]))                   # Expected: 1
print(solution().max_even_odd([]))                    # Expected: 0
print(solution().max_even_odd([1,2,4,6,3,5]))         # Expected: 2
print(solution().max_even_odd([1,2,3,4,5,6,7,8,10]))  # Expected: 8
print(solution().max_even_odd([-1,2,-3,4,-5]))        # Expected: 5
print(solution().max_even_odd([2,3,4,5,7,9,10,11,12]))# Expected: 4



