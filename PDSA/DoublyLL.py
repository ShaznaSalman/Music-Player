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
