#welcome message
user_name = input("Enter your name:")
print("Hello", user_name)

class Node:#Worst case ---> O(1)
    def __init__(self, info):
      self.info = info
      self.next = None
class SinglyLinkedList:#Worst case ---> O(N) wher n represents the number of nodes of the LL
      def __init__(self):
          self.head = None
          self.tail = None
      def isEmpty(self):#Worst case ---> O(1) #checks if the LL is empty
          return self.head == None
      def AddNode(self, info):#Worst case ---> O(1)
          new_node = Node(info)
          if not self.head:#if there is no nodes in the LL the head and the tail should poin to the added node
              self.head = new_node
              self.tail = new_node
          else:#else add the node at the and which will be the tail
              self.tail.next = new_node
              self.tail = new_node
      def DisplayNodes(self):#Worst case ---> O(N)
        if self.isEmpty():#to check if the LL is empty
            print("The linked list is empty")
            return
        current = self.head
        while current != None :#O(N)
            print(current.info, end=" ")
            current = current.next
      def search_and_delete_node(self,value):#Worst case ---> O(N)
            current = self.head
            prev = None
            while current:#O(N)
              if current.info == value:#at the first current will be pointing to the head which meens that prev points to none then if current.info = value then the value at the head will be removed
                  if prev:
                        prev.next = current.next
                        current.next = None
                  else:
                        self.head = current.next
                        current.next = None
                  print(current.info, "have been deleted from the linked list")
                  return
              else:
                  prev = current
                  current = current.next
            if self.head == None:# if self.head = None then there is no node in the LL
                print("Can't delete from empty linked list")
            else:#if the current pointer reached the end of the LL and pointed to none then the value was not found
                print("Value not found")
def displayMainMenu():#Worst case ---> O(1)
    print("1. Singly Linked List\n2. Check if Palindrome\n3. Priority Queue\n4. Evaluate an Infix Expression\n5. Graph\n6. Exit")
def main():
    sll = SinglyLinkedList()
    displayMainMenu()
    choice = int(input("Enter a number:"))
    counter = 0
    while choice != 6 and counter < 3:
        if choice == 1:
            while True:
                print("\nSingly Linked List Menu:")
                print("a. Add Node")
                print("b. Display Nodes")
                print("c. Search for & Delete Node")
                print("d. Return to main menu")
                sub_choice = input("Enter your choice: ")
                if sub_choice == 'a':
                    info = int(input("Enter the numerical value: "))
                    sll.AddNode(info)
                elif sub_choice == 'b':
                    sll.DisplayNodes()
                elif sub_choice == 'c':
                    value = int(input("Enter the value to search and delete: "))
                    sll.search_and_delete_node(value)
                elif sub_choice == "d":
                    break
                else:
                    print("Invalid choice. Try again.")