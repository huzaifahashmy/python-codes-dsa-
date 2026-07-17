#so basically a linked list is a object in which it has 
# two main things 
# its structure is mainly consists of two things -> 1. data , 2. next pointing object location 
# it consists of mainly these little two things -
# . creating the nodes 
# . connecting the nodes
# . traversing through each of it 


class node:
    def __init__(self , data):
        self.data = data 
        self.next = None

# creating the nodes 
first = node(10)
second = node(20)
third = node(30)

# connecting the nodes

first.next = second 
second.next = third 


# head of the linked list 
head = first 


temp = head

# now traverse 

while temp:
    print(temp.data , end= "->")
    temp = temp.next 


print ("None")

