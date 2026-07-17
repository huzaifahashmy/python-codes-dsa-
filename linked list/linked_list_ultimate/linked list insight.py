class Node:
    def __init__(self , data):
        self.item = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def constructor(self , numbers :list[int]):


        for nums in numbers:
            new_node = Node(nums)
            if self.head is None:
                self.head = new_node
            
            new_node.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.item , end= " ->")
            temp = temp.next
        print("None")
        



c1 = Node(10)
c2 = Node(20)
c3 = Node(30)

c1.next = c2
c2.next = c3
c3.next = None

print(c1.next.next.item)

temp = c1
while temp:
    print(temp.item , end= "->")

    temp = temp.next
    if temp is None:
        print("None")

# now we will be provided with a list of numbers , that we have to add it and
# make it to a linked list 

numbers = [1 , 2 ,3 ,4 ,5 ,6 ,7]





