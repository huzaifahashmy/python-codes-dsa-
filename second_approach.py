def arrange(arr):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]

    result = []
    i = j = 0

    while i < len(neg) and j < len(pos):
        
        result.append(pos[j])
        result.append(neg[i])
        i += 1
        j += 1

    # remaining elements
    result.extend(neg[i:])
    result.extend(pos[j:])

    return result


arr1 = [9, 4, -2, -1, 5, 0, -5, -3, 2]
print(arrange(arr=arr1))
