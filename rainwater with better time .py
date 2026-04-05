  
def water(arr):
    n = len(arr)
    left = [0]*n
    right = [0]*n
    res = 0
    # fill the left array
    left[0] = arr[0]
    for i in range(1 , n):
        left[i] = max(left[i - 1] , arr[i])
#   fill the right array
    right[n-1] = arr[n-1]
    for i in range(n-2 , -1 , -1):
        right[i] = max(right[i+1] , arr[i])
# 
    #calculating the accumulated eater element by eleme
    for i in range(1 , n-1):
        min_of_2 = min(left[i] , right[i])
        res += min_of_2 - arr[i]
    return res
if __name__ == "__main__":
    arr = [2 ,1,5,3,1,0,4,5,6,3,2,3,4,6,7,9,87,6,423,2,11,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
    print(water(arr=arr))\
    




