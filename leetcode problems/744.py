class Solution:

    def nextGreatestLetter(self, letters, target):

        letters.sort()

        for ch in letters:

            if ch > target:
                return ch

        return letters[0]




letters = ["c","f","j"]

target = "a"

print(Solution().nextGreatestLetter(letters , target= target))


