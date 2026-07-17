# presum of the array 

def presum(arr):
    n = len(arr)
    pre_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        pre_sum[i] = pre_sum[i - 1] + arr[i - 1]

    return pre_sum


class solution:

    def twoSum(self , nums:list[int] , target: int)-> list[int]:
        # just create a hashmap wiht dictionay 
        hashmap = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in hashmap:
                return [hashmap[needed] , i]

            else:
                hashmap[nums[i]] = i
                

nums = [11 , 2 , 7 , 15]

target = 9

print(solution().twoSum(nums= nums , target=target))


