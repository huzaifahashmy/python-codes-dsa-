class Solution:
    def minFlips(self, s):
        flip1 = 0  # for pattern 010101...
        flip2 = 0  # for pattern 101010...
        
        for i in range(len(s)):
            # expected characters
            if i % 2 == 0:
                expected1 = '0'
                expected2 = '1'
            else:
                expected1 = '1'
                expected2 = '0'
            
            if s[i] != expected1:
                flip1 += 1
            
            if s[i] != expected2:
                flip2 += 1
        
        return min(flip1, flip2)
    

    