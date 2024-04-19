#=============Circular Doubly Linked List===================

#----------------Display one value-------------
print("\n\nCIRCULAR DOUBLY LINKED LISTS\n\n")

# Define a Node class for circular doubly linked list
class NodeCircularDoubly:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

# Creating a single node
first = NodeCircularDoubly(3)
print("Displaying one value:")
print("Value in the first node:", first.data)
print("\n")

#-------------Display 2 values----------------

# Circular Doubly Linked List Class
class CircularDoublyLinkedList: 
    def __init__(self): 
        self.head = None

    # Add a node to the circular doubly linked list
    def add_node(self, data):
        new_node = NodeCircularDoubly(data)

        if not self.head:
            self.head = new_node
            new_node.prev = new_node  # Circular reference
            new_node.next = new_node  # Circular reference
        else:
            tail = self.head.prev  # Get the current tail
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node  # Update the new tail

    # Print the elements of the circular doubly linked list
    def print_list(self):
        current_node = self.head
        print("Displaying 3 values:")
        while True:
            print(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break

# Creating nodes with values
node1 = NodeCircularDoubly(2)
node2 = NodeCircularDoubly(1)
node3 = NodeCircularDoubly(3)

# Linking nodes together

node1.next = node2
node1.prev = node3  
node2.prev = node1
node2.next = node3  
node3.prev = node2  
node3.next = node1 

# Creating a circular doubly linked list with the head pointing to the first node
CDLL = CircularDoublyLinkedList()
CDLL.head = node1

# Printing the circular doubly linked list
CDLL.print_list()
print("\n")

#---------------------Insert---------------------------
print("Insert a value:")
print("\n")

# Circular Doubly Linked List Class for Insertion
class CircularDoublyLinkedListInsert:
    def __init__(self):
        self.head = None

    # Add a node to the circular doubly linked list
    def add_node(self, data):
        new_node = NodeCircularDoubly(data)

        if not self.head:
            self.head = new_node
            new_node.prev = new_node  # Circular reference
            new_node.next = new_node  # Circular reference
        else:
            tail = self.head.prev  # Get the current tail
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node  # Update the new tail

    # Print the elements of the circular doubly linked list
    def print_list(self):
        current_node = self.head
        print("Circular Doubly Linked List:")
        while True:
            print(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break

# Creating a circular doubly linked list with nodes
circular_list_insert = CircularDoublyLinkedListInsert()
circular_list_insert.add_node(10)
circular_list_insert.add_node(20)
circular_list_insert.add_node(30)

# Printing the circular doubly linked list
circular_list_insert.print_list()
print("\n")

#--------------------Delete----------------------------------------
print("Delete\n")
# Circular Doubly Linked List Class for Deletion
class CircularDoublyLinkedListDelete:
    def __init__(self):
        self.head = None

    # Add a node to the circular doubly linked list
    def add_node(self, data):
        new_node = NodeCircularDoubly(data)

        if not self.head:
            self.head = new_node
            new_node.prev = new_node  # Circular reference
            new_node.next = new_node  # Circular reference
        else:
            tail = self.head.prev  # Get the current tail
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node  # Update the new tail

    # Delete the first node of the list
    def delete_first_node(self):
        if not self.head:
            print("List is empty. Nothing to delete.")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

    # Print the elements of the circular doubly linked list
    def print_list(self):
        current_node = self.head
        
        while True:
            print(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break
print("Values\n")
# Creating nodes with values
circular_list_delete = CircularDoublyLinkedListDelete()
circular_list_delete.add_node(10)
circular_list_delete.add_node(20)
circular_list_delete.add_node(30)
circular_list_delete.add_node(40)

# Printing the circular doubly linked list
circular_list_delete.print_list()

# Deleting the first node
circular_list_delete.delete_first_node()
print("After deleting the first node\n")
circular_list_delete.print_list()
