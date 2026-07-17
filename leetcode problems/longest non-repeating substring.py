class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = set()

        count = 1
        for i in range(len(s)-1):
            if s[i]!= s[i+1]:
                count +=1 
            else:
                hashmap.add(count)

                count = 0
    
    def correct_appraoch(self , s:str)->int:
        hashmap = {}
        left = 0 
        right = 0 
        max_length = 0
        length = len(s)
        while(right < length):
        #     subarray = s[left:right+1]
        #     if s[right] not in subarray:
        #         hashmap[s[right]] = right
        #         right += 1
        #         max_length = max(max_length , right - left +1)
        #     else:
        #         left = hashmap[s[right]]+1
            
        # return max_length
            if s[right] in hashmap and hashmap[s[right]] >= left:
                left = hashmap[s[right]]+1

            hashmap[s[right]] = right

            max_length = max(max_length , right - left +1)

            right+=1

        return max_length
    




    

s = ""

print(Solution().correct_appraoch(s=s))







        # we will have to parse throuhg the given array , starting with the right pointer towards the right 



