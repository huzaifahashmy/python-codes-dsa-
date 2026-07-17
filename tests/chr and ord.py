def sortdtring(s :str):
    count = [0]*26
    for ch in s:
        count[ord(ch) - ord('a')] +=1 


    result = []

    # print(count)
    for i in range(26):
        if count[i] > 0:
            result.append(chr(i + ord('a')) * count[i])

    return ''.join(result)
    # i guess this thing will now work just as fine now 


    # the above code is the equivalent of this below code 
    #-> str.sort()
    # return ''.join(str)
    


print(sortdtring("huzaifa"))

