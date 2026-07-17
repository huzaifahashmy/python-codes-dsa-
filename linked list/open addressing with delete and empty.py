class hashtable():
    def __init__(self , size):
        self.size = size
        self.table = [-1]*size

    def insert(self, key):

        index = key % self.size # -> this is the curent insert hash that we are using 
        
        while self.table[index] != -1  and self.table[index] != -2:
            # this means that , the both the conditions needs to be satisfied after inserting the element 

            index = (index +1) % self.size



        self.table[index] = key
        

    def delete(self , key):
        index = key % self.size
        start = index


        while self.table[index] != -1 :


            if self.table[index] == key:
                self.table[index] = -2
                return True
            

            index = (index+1) % self.size
            
            if index == start:
                break 


        return False
                



ht = hashtable(10)
# ht.insert(1)

numbers = [1,2,3,4,5,6,7,8,9]

for nums in numbers:
    ht.insert(nums)
    
print(ht.table)

ht.delete(5)
ht.delete(7)
print(ht.table)

ht.insert(14)



print(ht.table)


