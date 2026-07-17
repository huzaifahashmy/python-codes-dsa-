class hashtable():
    def __init__(self , size):
        self.size = size
        self.table = [-1]*size
        self.prime = self.find_largest_prime()

    # now to implement a hash function which takes and handle the index 
    # through special functions

    # h1(key)   -> primary hash function 
    # h2(key)   -> secondary hash functions
    # i probe number -> which increases on the no. of collisions
    # hash(key,i)=(h1​(key)+i⋅h2​(key)) mod  m
    def is_prime(self, number):
        if number < 2:
            return False
        
        for i  in range( 2 , int(number ** 0.5) +1):
            if number % i == 0:
                return False
            

        return True
    

    def find_largest_prime(self):
        for nums in range(self.size -1  , 1 , -1):
            if self.is_prime(nums):
                return nums
            
        return 2 
    

    def h1(self , key):
        return key % self.size
    

    def h2(self, key):

        return self.prime - (key % self.prime)


    # first we will create a funciton hich checks weather the slot is empty or not ?

    def index_finder(self, key):

        for i in range(self.size):

            index = (
                self.h1(key)
                + i * self.h2(key)
            ) % self.size

            if self.table[index] in (-1, -2):
                # self.table[index] = key
                return index

        # print("Hash Table is Full!")
        # hash table is full
        return -3
    
    def insert(self , key):
        index = self.index_finder(key= key)
        if index == -3:
            print("hash table is full")
            return 
        
        self.table[index] = key 
        print("key inserted successfully")

        return
    

    def display(self):
        print(self.table)





numbers = [22,33,44,55,23,24,6,8,7]

ht = hashtable(8)

for nums in numbers:
    ht.insert(nums)

ht.display()



    







        
