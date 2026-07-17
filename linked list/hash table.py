import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    

    def modified_insert(self, data):

        if self.search(data):
            print("Duplicate found! Cannot insert.")
            return False

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return True

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        return True




    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        # if the head element is the main culprit

        
        while current.next:
            current = current.next
        current.next = new_node


    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def delete(self, key):
    # If list is empty
    
        if self.head is None:
            print("the list is empty")
            return
        # If head needs to be deleted
        if self.head.data == key:
            self.head = self.head.next
            print(f"element {key} has been deleted successfully")
            
            return
        current = self.head
        # Find the node before the one to delete
        while current.next and current.next.data != key:
            current = current.next
        # the current.next is used to handle error in python 
        # the current.next -> means that "Does a next node exist?"
        # If current.next is None, we cannot access:
        # If value found
        if current.next:
            current.next = current.next.next
            print("element deleted")
            # now to print the new list 
            # print("the new list")
            # self.display()
        else:
            print("the key element is not present ")

class hashtable:
    def __init__(self , bucket):
        self.bucket = bucket
        self.table = [LinkedList() for _ in range(bucket)]
        # we are creating a list of empty linked list 
        # so thats is the reaso why we are creating it

    
    def hashig_function(self, key):
        return key % self.bucket
    

    # in this hashing function we nee to understand what does this do 
    # ------------------------------------- # 
    # we use hashing fucntion to store values , and user that hashing fucntions again to retrieve that value 




    
    # now comed the part in which we have to insert some values inside the hashed 
    # bucket's table 

    def insert(self ,key):
        index = self.hashig_function(key)
        if self.table[index].modified_insert(key):
            print("element addedd")
            return True
        else:
           print("cannot be added")
           return False
        # self.table[index].insert(key)
        # now please pay here extra attention 
        # what we have done over here 
        # we have used two functions at once 
        # 1. table 
        # 2. insert    -> we have used the table function to access the table and after that we have passed the index to access that particulat linked list 
        # and then finnaly inserted that key in that linked list 


    def  search(self , key):
        index = self.hashig_function(key)
        return self.table[index].search(key)
    

    # now to display the whole table at once

    def display(self):
        for i in range(self.bucket):
            print(f"bucket{i}: ", end= "")
            current = self.table[i].head
            while current:
                print(current.data , end= " ->")
                current = current.next

            print("none")
    # now to also implement delete function as well 


    def delete(self , key):
        index = self.hashig_function(key)
        return self.table[index].delete(key)
    
        
    def find_biggest_collsion(self):
        biggest = 0 

        for i in range(self.bucket):
            count = 0
            current = self.table[i].head
            while current:
                count +=1 
                current = current.next

            biggest = max(biggest, count)

        print(biggest)

        return
    
    # def insert1(self , key):

    # now to modify the insert function , which doesent takes any duplicate elements in it 

    




# so to handle the collision , we simply implement ways such as chaining like ->  "LINKED LIST"
# an example question to find out the biggest collision table's length 





# this above us , we have utlized full raandint and list comprehention all at once



# for k in numbers:
#     ht.insert(k)

# ht.display()
# # ht.find_biggest_collsion()
# ht.delete(3)
# ht.display()




class user_defined():
    def collisions(self , key, bucket):
        # just to create a empty list 
        collide = [0]*bucket
        no_collisions = 0

        for nums in key:
            indx = nums%bucket
            collide[indx] += 1
        # now that we have created a list of collisions 
        # now we have to retrieve it and count the no. of collisions 
        # if it is bigger than one, then we have to ount the occurance -1 


        for i in range(bucket):
            if collide[i] > 1:
                no_collisions += (collide[i] -1)

        return no_collisions
    

# key , bucket = [15, 11, 27, 8, 12, 22], 7

key = [ 15, 22, 37, 49, 58, 63, 71, 84, 95, 101, 118, 127, 134, 145, 156, 167, 178, 189, 200, 211, 222, 233, 244, 255, 266, 277, 288, 299, 310, 321 ,15 ] 
bucket = 11

ht = hashtable(10)


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16 , 15]


for num in numbers:
    ht.insert(num)






