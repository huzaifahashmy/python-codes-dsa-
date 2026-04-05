arr = [1,2]


# frequency = {}

# count_majority = 0
# # for i in arr:
# #     if i not in frequency:
#         frequency[i] = 1

#     else:
#         frequency[i] += 1


# for i in frequency:
#     if frequency[i] > (len(arr) / 2):
#         print(i)



def get_majority(arr):
    frequency = {}
    for i in arr:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] +=1
    for i in frequency:
        if frequency[i] > (len(arr) / 2):
            return i 
        
    return -1

print(get_majority(arr=arr))



