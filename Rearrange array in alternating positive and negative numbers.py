def arrange(arr) ->list:

    finale = [0]*len(arr)
    positve = []
    negative = []
    for i in arr:
        if i > 0:
            positve.append(i)

        else:
            negative.append(i)
            

    negative_index = 0
    positive_index = 0

    for i in range(len(arr)):
        if i%2 != 0:
            if negative_index < len(negative):

                finale[i] = negative[negative_index]
                negative_index += 1

        else:
            if positive_index < len(positve):

                finale[i] = positve[positive_index]
                positive_index +=1

    return finale



arr1 = [9, 4, -2, -1, 5, 0, -5, -3, 2]

print(arrange(arr=arr1))




        