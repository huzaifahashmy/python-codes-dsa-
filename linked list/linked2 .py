class Node:
    # this is the function were we have to vreate the linked list 
    
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to create linked list
def create_linked_list(arr):

    head = Node(arr[0])
    current = head

    for value in arr[1:]:
        current.next = Node(value)    # this line right here is pretty important , and is use to traverse through each element of the array and create a linked list 

        current = current.next     # thsi sets the prevoius element in the array as the next element , through the use of the current.next 


    return head


# Traverse function
def print_list(head):

    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("None")


arr = [10, 20, 30, 40, 50]

head = create_linked_list(arr)

print_list(head)