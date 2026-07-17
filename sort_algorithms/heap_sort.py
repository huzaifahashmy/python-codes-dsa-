def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1    #  the left child of the node
    right = 2 * i + 2   # the right child of the node

    # check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # check right child
    if right < n and arr[right] > arr[largest]:
        largest = right


    # th key intuition over here is simple 
    # what we are trying to do is that , 
    # we are trying to find the max element out of the parent -> and their childs

    # swap if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr , k):
    n = len(arr)
    # a bvbery good thing to cath over here is that we are only creaint a implicit binary tree over here

    # build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
     

    # it builds from bottom to top 

    # what this funciton does ? this only returns the max from the binary array and move it to up


    # print(arr)

    # extract elements
    for i in range(n - 1, 0, -1):  # length -> to  first element 
        # now we have the element in the array , we just need to return the kth element
        if  i == k:
            return arr[0]
        
        arr[0], arr[i] = arr[i], arr[0]  # move max to end
        # if n == kth elemetn -> return the kth  element 
        # if i == n - k:
        #     return arr[i] 
        

        heapify(arr, i, 0) 
        # we need to move the largest element to the top
        # and will move to the max element to the last 
        # and will not touch the last elements , we wil only access the new remaining elements

        # and need to call the the heapify repeatedly


    return arr


print(heap_sort([3, 3, 9, 10, 27, 38, 43, 43, 50, 82, 89, 100, 323] , 5))