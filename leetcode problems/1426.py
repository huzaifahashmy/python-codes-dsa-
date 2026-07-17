class solution():
    def count(self , numbers:list[int] ) ->int:

        hashset = set(numbers)

        # for num in numbers:
        #     hashset[num] = hashset.get(num , 0) +1
        county =0
        # return hashset
        for num in hashset:
            if num+1 in hashset:
                county +=1 

        return county
    

# so like this is not a stable approach 


    def second(self , numbers:list[int]) -> int:
        if not numbers: 
            return 0 
        
        ans = 0
        length = 0

        hashset = set(numbers)
        for numbers in hashset:
            # now check weather the number is the startingg of the sequence

            if numbers-1 not in hashset:
                while (numbers + length)  in hashset:
                    length += 1 

            ans = max(ans , length)

        return ans 
    
nums = [100, 4, 200, 1, 3, 2, 50]
print(solution().second(nums))



