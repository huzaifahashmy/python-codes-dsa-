# Creating a Node
class Node:
    def __init__(self, data):
        self.data = data      # stores the value
        self.next = None      # points to next node


        # here the self means the current object 
        # for example n1.data = 10
        # data = 10
        # self = the current object (n1)

# Creating the Linked List
class LinkedList:
    def __init__(self):
        self.head = None      # first node of the list
        # note that , this above code only executes once when the object is created , so the head is None at the start of the program
        

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)   # creating a node
        

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node    # now to insert in on the last occuring of the node


    # Display the linked list
    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # Search for a value
    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return True
            current = current.next

        return False

    # Delete a node
    def delete(self, key):

        # If list is empty
        if self.head is None:
            print("the list is empty")
            return

        # If head needs to be deleted
        if self.head.data == key:
            self.head = self.head.next
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
            print("the new list")
            self.display()


        else:
            print("the key element is not present ")

# -----------------------------
# Using the Linked List
# -----------------------------

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)


# ll.display()

# ll.delete(4)



# now to create a whole new menu bar system in the terminal

while True:
    print("\n" + "=" * 40)
    print("       LINKED LIST MENU")
    print("=" * 40)
    print("1. Insert Element")
    print("2. Display List")
    print("3. Delete Element")
    print("4. Search Element")
    print("5. Exit")
    print("=" * 40)

    choice = input("Enter your choice: ")

    if choice == "1":
        value = input("Enter element to insert: ")
        ll.insert(value)
        print(f"✓ '{value}' inserted successfully.")

    elif choice == "2":
        print("\nCurrent Linked List:")
        print("-" * 40)
        ll.display()

    elif choice == "3":
        value = input("Enter element to delete: ")
        ll.delete(value)

    elif choice == "4":
        value = int(input("Enter element to search: "))

        if ll.search(value):
            print(f"✓ '{value}' found in the list.")
        else:
            print(f"✗ '{value}' not found in the list.")

    elif choice == "5":
        print("\nThank you for using Linked List Manager!")
        break

    else:
        print("✗ Invalid choice. Please try again.")


        '''hello  this is a basic comment in python using the triple quotes'''

