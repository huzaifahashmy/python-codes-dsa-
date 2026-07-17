class solution():
    def divide(self , arr:list[int]):
        
        first = arr[0]
        smallest = float("inf")
        second = float("inf")

        for nums in arr[1:]:
            if nums < smallest:
                second = smallest
                smallest = nums


            elif nums < second:
                second = nums



        return first + smallest + second
    



nums = [1, 3, 2, 4]


print(solution().divide(arr= nums))


