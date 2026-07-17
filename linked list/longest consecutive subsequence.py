class Solution:

    def longestConsecutive(self, arr):

        lookup = set(arr)
        longest = 0

        for num in lookup:

            # Is this the start of a sequence?
            if num - 1 not in lookup:

                current = num
                length = 1

                while current + 1 in lookup:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
    
    def count_distinct_window(self , arr , k):

        output = []
        for i in range(len(arr) - k + 1):
            window = arr[i: i+k]

            output.append(len(set(window)))

        return output
    




        


        


# arr = [15, 13, 12, 14, 11, 10, 9] # expected ans -> 7 



# print(Solution().longestConsecutive(arr= arr))
arr = [1, 2, 1, 3, 4, 2, 3]

print(Solution().count_distinct_window(arr= arr , k= 4))












    