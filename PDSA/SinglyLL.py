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
