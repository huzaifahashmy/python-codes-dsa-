arr1 = [1,2,3,4,5,6,7,8,9]

arr2 = [8,9,10,11]


# intersection here means . totally common out elements between the two arrays 

def union(a , b):
    return len(set(a) or set(b))


print(union(arr1 , arr2))





