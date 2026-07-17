class solution():
    def sorting(self , arr , x):
        # first we wil create the array with the difference

        pairs = [(abs(a - x) , a ) for a in arr]
        # the above is also known as list comprehension 
        pairs.sort()

        result = [a  for _, a in pairs]
        print (result)
        return result
    







solution().sorting([10, 5, 3, 9, 2] , 7)





    


