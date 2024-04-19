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
