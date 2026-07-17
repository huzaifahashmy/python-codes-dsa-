class hashtable :
    def __init__(self , size):
        self.size = size
        self.table = [None]* size

    def insert(self , key):
        index = key % self.size
        while self.table[index] is not None:
            index = (index +1 )%self.size

        self.table[index] = key

    # one of the most efficient technique is to skip the none elements and to add it to the element next to the on none element 
    # also known as linear addressing technique
    
    def display(self):
        print(self.table)

    def search(self, key):
        index = key % self.size

        while self.table[index] is not None:
            if self.table[index] == key:
                return True
        
            index =  (index +1 ) % self.size

        return False
    




nums = [2,3,4,22,33,23,4,56]

ht  = hashtable(10) 

# and in open addressing , the size of the hash table has to be larger than or equal to the size of the data


for num in nums:
    ht.insert(num)


if ht.search(22):
    print("element is present")
else:
    print("element is not present")




