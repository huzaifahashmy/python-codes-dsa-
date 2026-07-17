class solution():
    # brute force approach
    def count_majority(self , nums:list[int] , target:int) -> int:

        n  = len(nums)

        ans = 0 
        for i in range(n):
            count = 0 

            for j in range(i , n):

                if nums[j] == target:
                    count +=1 

                length = j - i +1 

                if count > length // 2:

                    ans +=1 

        return ans 
    

    def count_majority_optimised(self , nums:list[int] ,target:int ):
        
    


nums = [1,2,2,3]

target = 2

print(solution().count_majority(nums= nums , target= target))

