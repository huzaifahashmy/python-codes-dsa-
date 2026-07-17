class computer:
    def __init__(self , data):   # this works as a constructor
        self.name = "huzaifa"
        self.age = data

    def update(self):
        self.age = 30

    def compare(self , other):
        if self.age == other.age:
            return True
        else:
            return False
        





c1 = computer(10)
c1.age = 100


c3 = computer(30)

if c1.compare(c3):
    print("they are same")
else:
    print("they are not")




print(c1.age)







