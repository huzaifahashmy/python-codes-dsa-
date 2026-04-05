left = 0 
right = 1 
target = 9
sum = 0



arr = [2,7,11,15]

for i in range(len(arr)):
    
    if sum == target:
        print([left +1 ,right -1])
        break
    elif sum > target:
        sum -= arr[i]
        right +=1
        left += 1
        # print([left , right])
    elif sum < target:
        sum += arr[i]
        right +=1
    else:
        print("nothing")



