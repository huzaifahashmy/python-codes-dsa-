def merge(arr):
    for i in range(len(arr)):
        start = arr[i][0]
        end = arr[i][1]

        middle_value = list(range(start + 1, end))

        
        print(list(range(start + 1, end)))

merge([[1, 3], [2, 4], [6, 8], [9, 10]])

def test(arr, find):
    for sub in arr:
        if find in sub:  # if it isfound , then we basically have to merge those two together up 
            
            return True
    return False

print(test([[1, 3], [2, 4], [6, 8], [9, 10]], 2))



def merge_intervals(arr):
    arr.sort()
    merged = []

    for interval in arr:
        if not merged or interval[0] >= merged[-1][1]: # If the current interval does not overlap with the last merged interval, add it to the merged list
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])  # If there is an overlap, merge the current interval with the last merged interval by updating the end time

    return merged



def merge_2(a, b):

    # to calculate the median of the two arrays we have to merge them together first and then we can calculate the median of the merged array

    median = 0 
    
    leny = len(a) + len(b)

    merged = a + b

    if leny % 2 == 0:
        median = (merged[leny//2 - 1] + merged[leny//2]) / 2
    else:
        median = merged[leny//2]

    return median



    # havr to calculate the median of the two arrays




print(merge_2([1, 3, 5], [2, 4, 6]))




