#=============Singly Linked List===================

#----------------Display one value-------------
print("SINGLY LINKED LISTS\n\n")

class NodeSingly:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Creating a single node
first = NodeSingly(3)
print("Displaying one value:")
print("Value in the first node:", first.data)
print("\n")

#-------------Display 2 values----------------

class LinkedListSingly: 
    def __init__(self): 
        self.head = None

    def print_list(self):
        current_node = self.head
        print("Displaying two values:")
        while current_node:
            print(current_node.data)
            current_node = current_node.next

# Creating nodes with values
node2 = NodeSingly(2)
node1 = NodeSingly(3)

# Linking nodes together
node1.next = node2

# Creating a linked list with the head pointing to the first node
LLSingly = LinkedListSingly()
LLSingly.head = node1

# Printing the linked list
LLSingly.print_list()
print("\n")

#---------------------Insert---------------------------
print("Insert  value")
print("\n")

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        newNode = NodeSingly(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def display(self):
        current = self.head

        if self.head is None:
            print("List is empty")
            return
        print("Displaying nodes of singly linked list:")
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

sList = SinglyLinkedList()

# Add nodes to the list
sList.addNode(1)
sList.addNode(2)
sList.addNode(3)
sList.addNode(4)

# Display the nodes present in the list
sList.display()
print("\n")

#------------Delete---------------------
print("Delete\n")
class LinkedListSinglyDelete:
    def __init__(self):
        self.head = None

    # Add new element at the end of the list
    def push_back(self, newElement):
        newNode = NodeSingly(newElement)
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode

    # Delete first node of the list
    def pop_front(self):
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None

    # Display the content of the list
    def PrintList(self):
        temp = self.head
        if(temp != None):
            while (temp != None):
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")

MyListSinglyDelete = LinkedListSinglyDelete()

# Add four elements in the list.
print("Before deleting")
MyListSinglyDelete.push_back(10)
MyListSinglyDelete.push_back(20)
MyListSinglyDelete.push_back(30)
MyListSinglyDelete.push_back(40)
MyListSinglyDelete.PrintList()
print("\n")

# Delete the first node
print("After deleting")
MyListSinglyDelete.pop_front()
MyListSinglyDelete.PrintList()
print("\n")

#=============Doubly Linked List===================

#----------------Display one value-------------
print("DOUBLY LINKED LISTS\n\n")

class NodeDoubly:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

# Creating a single node
first = NodeDoubly(3)
print("Displaying one value:")
print("Value in the first node:", first.data)
print("\n")

#-------------Display 2 values----------------

class LinkedListDoubly: 
    def __init__(self): 
        self.head = None

    def print_list(self):
        current_node = self.head
        print("Displaying 3 values:")
        while current_node:
            print(current_node.data)
            current_node = current_node.next


# Creating nodes with values
node1 = NodeDoubly(2)
node2 = NodeDoubly(1)
node3 = NodeDoubly(3)

# Linking nodes together
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

# Creating a linked list with the head pointing to the first node
LLDoubly = LinkedListDoubly()
LLDoubly.head = node1

# Printing the linked list
LLDoubly.print_list()

print("\n")

#---------------------Insert---------------------------
print("Insert  value")
print("\n")

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        newNode = NodeDoubly(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def display(self):
        current = self.head

        if self.head is None:
            print("List is empty")
            return
        print("Displaying nodes of doubly linked list:")
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

dList = DoublyLinkedList()

# Add nodes to the list
dList.addNode(1)
dList.addNode(2)
dList.addNode(3)
dList.addNode(4)
dList.addNode(5)

# Display the nodes present in the list
dList.display()
print("\n")

#------------Delete---------------------
print("Delete\n")

class DoublyLinkedListDelete:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add new element at the end of the list
    def push_back(self, newElement):
        newNode = NodeDoubly(newElement)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    # Delete the first node of the list
    def pop_front(self):
        if self.head is not None:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

    # Display the content of the list
    def PrintList(self):
        temp = self.head
        if temp is not None:
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")

MyListDoublyDelete = DoublyLinkedListDelete()

# Add five elements to the list.
print("Before deleting")
MyListDoublyDelete.push_back(10)
MyListDoublyDelete.push_back(20)
MyListDoublyDelete.push_back(30)
MyListDoublyDelete.push_back(40)
MyListDoublyDelete.push_back(50)
MyListDoublyDelete.PrintList()
print("\n")

# Delete the first node
print("After deleting the first node")
MyListDoublyDelete.pop_front()
MyListDoublyDelete.PrintList()
print("\n")

#=============Circular Singly Linked List===================

#----------------Display one value-------------
print("CIRCULAR SINGLY LINKED LISTS\n\n")

class NodeCircularSingly:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Creating a single node
first = NodeCircularSingly(3)
first.next = first  # Circular reference

print("Displaying one value:")
print("Value in the first node:", first.data)
print("\n")

#-------------Display 2 values----------------

class CircularSinglyLinkedList: 
    def __init__(self): 
        self.head = None

    def print_list(self):
        current_node = self.head
        print("Displaying three values:")
        while True:
            print(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break

# Creating nodes with values
node3 = NodeCircularSingly(30)
node2 = NodeCircularSingly(20)
node1 = NodeCircularSingly(10)

# Linking nodes together
node1.next = node2
node2.next = node3
node3.next = node1  # Circular reference

# Creating a circular linked list with the head pointing to the first node
CLLSingly = CircularSinglyLinkedList()
CLLSingly.head = node1

# Printing the circular linked list
CLLSingly.print_list()
print("\n")

#---------------------Insert---------------------------
print("Insert a value")
print("\n")

class CircularSinglyLinkedListInsert:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = NodeCircularSingly(data)

        if not self.head:
            self.head = new_node
            self.head.next = self.head  # Circular reference
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break

# Creating a circular singly linked list with nodes
circular_list_insert = CircularSinglyLinkedListInsert()
circular_list_insert.add_node(10)
circular_list_insert.add_node(20)
circular_list_insert.add_node(30)

# Printing the circular singly linked list
print("Circular Singly Linked List:")
circular_list_insert.print_list()
print("\n")

#--------------------Delete----------------------------------------
print("Delete\n")
class CircularSinglyLinkedListDelete:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = NodeCircularSingly(data)

        if not self.head:
            self.head = new_node
            self.head.next = self.head  # Circular reference
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

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

    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break

# Creating nodes with values
circular_list_delete = CircularSinglyLinkedListDelete()
circular_list_delete.add_node(10)
circular_list_delete.add_node(20)
circular_list_delete.add_node(30)
circular_list_delete.add_node(40)

# Printing the circular singly linked list

circular_list_delete.print_list()
print("\n")
# Deleting the first node
circular_list_delete.delete_first_node()
print("After deleting the first node\n")
circular_list_delete.print_list()


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
