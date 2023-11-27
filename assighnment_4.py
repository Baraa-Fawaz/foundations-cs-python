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
class Stack:#Worst case ---> O(1)
    def __init__(self):
        self.data = []
    def push(self, data):
        self.data.append(data)#adds the element to the list
    def pop(self):
        return self.data.pop()#removes the last pushed element to the list
    def peek(self):#see the last element of the list without removing it
        return self.data[len(self.data)-1]
    def is_empty(self):#checks if the list is empty
        return len(self.data) == 0

def checkPalindrome(s):#Worst case ---> O(N) where N represents the length of the string
    stack = Stack()
    for char in s:#Worst case ---> O(N) #appends every character in the string to the stack
        stack.push(char)
    for char in s:#Worst case ---> O(N) #check if the first char in the string = to the last char in the stack and remove it
        if char != stack.pop():
            return False
    return True

class Stack:#Worst case ---> O(1)
    def __init__(self):
        self.data = []
    def push(self, data):
        self.data.append(data)#adds the element to the list
    def pop(self):
        return self.data.pop()#removes the last pushed element to the list
    def peek(self):#see the last element of the list without removing it
        return self.data[len(self.data)-1]
    def is_empty(self):#checks if the list is empty
        return len(self.data) == 0

class Student:#Worst case ---> O(1)
    def __init__(self, name, midterm_grade, final_grade, good_attitude):
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.good_attitude = good_attitude

class PriorityQueue:#Worst case ---> O(N)
    def __init__(self):#Worst case ---> O(1)
        self.head = None
        self.tail = None
        self.size = 0

    def displayNodes(self):#Worst case ---> O(N)
        current = self.head
        while current != None:
            print(current.info)
            current = current.next
    def enqueue(self, student):#Worst case ---> O(N)
        node = Node(student)
        if self.size == 0:#the LL is empty the head and tail should point to the node
            self.head = node
            self.tail = node
            self.size += 1

        else:
            if node.info.good_attitude == True:# check if the added student has a goode attitued
                if self.head.info.good_attitude == False:# if the student at the head has bad attitued then add the new student to the head
                    node.next = self.head
                    self.head = node
                    self.size += 1
                else:#we need to check the final grades
                    if node.info.final_grade > self.head.info.final_grade:# if the student at the head has less final grade then add the new student to the head
                        node.next = self.head
                        self.head = node
                        self.size += 1
                    elif node.info.final_grade == self.head.info.final_grade:# if the student at the head has = final grade then check the mid grades
                        if node.info.midterm_grade > self.head.info.midterm_grade: # if the student at the head has less mid grade then add the new student to the head
                            node.next = self.head
                            self.head = node
                            self.size += 1
                    else:# if the student at the head has higher final grade then add the new student to the head
                        current = self.head
                        while current.next and current.next.info.good_attitude  == True and current.next.info.final_grade > node.info.final_grade  and node.info.midterm_grade <= current.next.info.midterm_grade :#to check where to add the node #O(N)
                            current = current.next
                        node.next = current.next
                        current.next = node
                        self.size += 1
            else:#the student dont have good attitued so add it to the tail
                self.tail.next = node
                self.tail = node
                self.size += 1
    def dequeue(self):#Worst case ---> O(1)
        if self.size == 0:
            print("Your Queue is Empty! Add a student first.")
        elif self.size == 1:
            student = self.head.info.name
            self.head = None
            self.tail = None
            self.size -= 1
            print("We are interviewing:", student)

        else:
            student = self.head.info.name
            self.head = self.head.next
            self.size -= 1
            print("We are interviewing:", student)

def evaluateAnInfixExpression(expression):#Worst case ---> O(N^2)
    stack_numbers = Stack()#initializing 2 stacks one for numbers and 1 for operators
    stack_operators = Stack()

    operators = set("+-*/")#to check if a char is an operator

    def precedence(operator):# O(1) #This function will give higher priority to *and/ by returning 2 then for + and - by returning 1
        if operator in "*/":
            return 2
        elif operator in "+-":
            return 1
        return 0

    def apply_operator(operator, operand1, operand2):# O(1) # the function will take two operands and performs the arethmatic operation then return it
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2

    for char in expression:#O(N) # starting by eterating through the whole exprission
        if char.isdigit():# check if the char is a digit it pushes it to the stack for numbers
            stack_numbers.push(int(char))
        elif char in operators:# check if the char is an operater
            while not stack_operators.is_empty() and precedence(stack_operators.peek()) >= precedence(char):#O(N)
                operator = stack_operators.pop()
                operand2 = stack_numbers.pop()
                operand1 = stack_numbers.pop()
                result = apply_operator(operator, operand1, operand2)
                stack_numbers.push(result)
            stack_operators.push(char)
        elif char == "(":# if the char is "(" we push it to the stack operator)
            stack_operators.push(char)
        elif char == ")":# if the char is "(" we perform the operation btw "(" and ")" py popping the operator at the top and popping the two numbers in the stack-numbers and then push the result to the stack_numbers
            while stack_operators.peek() != "(":#O(N)
                operator = stack_operators.pop()
                operand2 = stack_numbers.pop()
                operand1 = stack_numbers.pop()
                result = apply_operator(operator, operand1, operand2)
                stack_numbers.push(result)
            stack_operators.pop()  # Pop the corresponding "("

    while not stack_operators.is_empty():#O(N)
        operator = stack_operators.pop()
        operand2 = stack_numbers.pop()
        operand1 = stack_numbers.pop()
        result = apply_operator(operator, operand1, operand2)
        stack_numbers.push(result)
    if not stack_numbers.is_empty():
      return stack_numbers.pop()
    else:
      return None

class LinkedList:#Worst case ---> O(N)
    def __init__(self):
        self.head = None
        self.next = None
        self.size = 0
    def addNode(self, data):#Worst case ---> O(1)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def deleteNode(self, data):#Worst case ---> O(N)
        current = self.head

        # when the node to be deleted is the head
        if current is not None and current.info == data:
            self.head = current.next
            return

        # Search for the node to be deleted
        prev = None
        while current is not None and current.info != data:#O(N)
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        self.size -= 1







class Graph:#Worst case ---> O(V)
    def __init__(self):
        self.vertices = {}
    def addVertex(self, vertex):#Worst case ---> O(1)
        if vertex not in self.vertices:#if the vetex does not already exists and that vertex as a ley to self.vertices and the LL as a value
            self.vertices[vertex] = LinkedList()
            return
        print("Vertex", vertex, "already exists")

    def addEdge(self, vertex1, vertex2):#Worst case ---> O(1)
        if vertex1 in self.vertices and vertex2 in self.vertices:# if the 2 verties the user wants to add an an edge btw them are found in self.vertisies the add a node of vertex 2 to vertex 1 and vise versal
            self.vertices[vertex1].addNode(vertex2)
            self.vertices[vertex2].addNode(vertex1)
        elif vertex1 not in self.vertices and vertex2 not in self.vertices:
            print("Vertices", vertex1, "and", vertex2, "do not exist to add the edge")
        elif vertex1 not in self.vertices:
            print("Vertex", vertex1, "does not exist to add the edge")
        else:
            print("Vertex", vertex2, "does not exist to add the edge")
    def removeVertex(self, vertex):#Worst case ---> O(V)
        if vertex in self.vertices: #if the vertex is found in self.vertices we delete it and the loop through all othor verticies and delet the node corresponing to that vertez if found
            del self.vertices[vertex]
            for v in self.vertices:
                self.vertices[v].deleteNode(vertex)
        else:
            print(vertex, "does not exists")

    def removeEdge(self, vertex1, vertex2):#Worst case ---> O(V)
        if vertex1 in self.vertices and vertex2 in self.vertices:# if the 2 verticies found in self.vertecies delete node 1 from vertex 2 and vise versal
            self.vertices[vertex1].deleteNode(vertex2)
            self.vertices[vertex2].deleteNode(vertex1)

    def display_vertices_with_degree(self, degree):#Worst case ---> O(1)
        result = []
        for vertex in self.vertices:#the size represents the number of edges to the vertes so if it is >= degree we append the vertex to the result
            if self.vertices[vertex].size >= degree:
                result.append(vertex)
        return result
    
    
def displayMainMenu():#Worst case ---> O(1)
    print("1. Singly Linked List\n2. Check if Palindrome\n3. Priority Queue\n4. Evaluate an Infix Expression\n5. Graph\n6. Exit")
def main():# O(N^2)
    sll = SinglyLinkedList()
    pq = PriorityQueue()
    graph = Graph()
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
        elif choice == 2:
            string = input("Enter the string:")
            print(checkPalindrome(string))
        elif choice == 3:
            while True:
                print("a. Add a student")
                print("b. Interview a student")
                print("c. Return to main menu")
                sub_choice = input("Enter your choice: ")

                if sub_choice == "a":
                    name = input("Enter the student's name: ")
                    midterm_grade = int(input("Enter the midterm grade (0-100): "))
                    final_grade = int(input("Enter the final grade (0-100): "))
                    good_attitude = input("Does the student have a good attitude? (true/false): ")
                    if good_attitude == "true":
                        good_attitude = True
                    else:
                        good_attitude = False
                    student = Student(name, midterm_grade, final_grade, good_attitude)
                    pq.enqueue(student)
                elif sub_choice == "b":
                    pq.dequeue()
                elif sub_choice == "c":
                    break
                else:
                    print("Invalid choice. Try again.")
        elif choice == 4:
            expression = input("Enter an infix expression: ")
            print("The answer of your infix expression is :", evaluateAnInfixExpression(expression))
        elif choice == 5:
            while True:
                print("5. Graph")
                print("a. Add vertex")
                print("b. Add edge")
                print("c. Remove vertex")
                print("d. Remove edge")
                print("e. Display vertices with a degree of X or more.")
                print("f. Return to main menu")
                sub_choice = input("Enter your choice: ")
                if sub_choice == 'a':
                    vertex = input("Enter the vertex: ")
                    graph.addVertex(vertex)
                    
                elif sub_choice == 'b':
                    vertex1 = input("Enter the first vertex: ")
                    vertex2 = input("Enter the second vertex: ")
                    graph.addEdge(vertex1, vertex2)
                    

                elif sub_choice == 'c':
                    vertex = input("Enter the vertex to remove: ")
                    graph.removeVertex(vertex)
                    

                elif sub_choice == 'd':
                    vertex1 = input("Enter the first vertex: ")
                    vertex2 = input("Enter the second vertex: ")
                    graph.removeEdge(vertex1, vertex2)
                    

                elif sub_choice == 'e':
                    degree = int(input("Enter the degree: "))
                    vertices = graph.display_vertices_with_degree(degree)
                    print("Vertices with a degree of ",degree, " or more:",vertices)
                    
                elif sub_choice == 'f':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice != 6:
            print("Invalid input")
            counter += 1
        displayMainMenu()
        choice = int(input("Enter a number:"))
    print("Exited,Good bye")

main()