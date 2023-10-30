user_name = input("Enter your name: ")
print("Hello", user_name)
#Welcome statment
def addMatrices(mat_1, mat_2):
    #for matrix_1
    row_1 = eval(input("Enter number of rows of the first matrix: "))
    column_1 = eval(input("Enter number of columns of the first matrix : "))
    mat_1 = []
    for i in range(row_1):
        mat_1.append([])#add an empty list which represent the rows
    for i in range(row_1):
        for j in range(column_1):
            mat_1[i].append(j)# Initialize the rows with values
    for i in range(row_1):
        for j in range(column_1):
            print("Enter the value in row", i +1, "col", j +1)
            mat_1[i][j] = int(input())#input the print statment as an integer
    print("you first matrix is",mat_1)
        #for matrix_2
    row_2 = eval(input("Enter number of rows of the second matrix: "))
    column_2 = eval(input("Enter number of columns of the second matrix : "))
    mat_2 = []#add an empty list which represent the rows
    for i in range(row_2):
        mat_2.append([])
    for i in range(row_2):
        for j in range(column_2):
            mat_2[i].append(j)# Initialize the rows with values
    for i in range(row_2):
        for j in range(column_2):
            print("enter the value in row", i + 1, "col", j + 1)
            mat_2[i][j] = int(input())#input the print statment as an integer
    print("you second matrix is", mat_2)
    if row_1 != row_2 or column_1 != column_2:
    print("Matrix addition is not possible. The matrices must have the same dimensions.")
    return #terminate the function if the dimentions of the two lists are different
    result = []
    for i in range(row_2):
        result_row = []
        for j in range(column_2):
            sum = mat_1[i][j] + mat_2[i][j]#adds the elements at same index
            result_row.append(sum)
        result.append(result_row)

    print("The result of matrix addition is:")
    print(result)
def checkRotation(m1, m2):
    #take the two functions from the user in the same way use at the first function
    row_1 = eval(input("Enter number of rows of the first matrix: "))
    column_1 = eval(input("Enter number of columns of the first matrix : "))
    mat_1 = []
    for i in range(row_1):
        mat_1.append([])
    for i in range(row_1):
        for j in range(column_1):
            mat_1[i].append(j)
    for i in range(row_1):
        for j in range(column_1):
            print("enter the value in row", i + 1, "col", j + 1)
            mat_1[i][j] = int(input())
    print("you first matrix is", mat_1)
    row_2 = eval(input("Enter number of rows of the second matrix: "))
    column_2 = eval(input("Enter number of columns of the second matrix : "))
    mat_2 = []
    for i in range(row_2):
        mat_2.append([])
    for i in range(row_2):
        for j in range(column_2):
            mat_2[i].append(j)
            mat_2[i][j] = 0
    for i in range(row_2):
        for j in range(column_2):
            print("enter the value in row", i + 1, "col", j + 1)
            mat_2[i][j] = int(input())
    print("you second matrix is", mat_2)
    #check if the two lists are rotational
    check_list = []
    if len(mat_1)>len(mat_2) or len(mat_2)>len(mat_1):# inorder for the two lists two be rotational then length of one of them should be greater than the other
        if len(mat_1)>len(mat_2):#if len mat_1 is greater than mat_2 the mat_1 has more rows than mat_2
           more_columns = mat_2
           more_rows = mat_1

        else:#if len mat_1 is less than mat_2 the mat_2 has more rows than mat_1
            more_rows = mat_2
            more_columns = mat_1
        for i in range(len(more_rows[0])):
          for j in range(len(more_rows)):
            check_list.append(more_rows[j][i])
          if check_list == more_columns[i]:#compers the first element of each row of the matrix having more rows to the first row in the second matrix
           return True, "the two matrices are rotational"
    return False, "the two matrices are not rotational"
def invertedDictionary(dictt):#O(N)
    inverted_dict = {}
    #create the initial dictionary
    num = int(input("Enter how many elements are there in the dictionary: "))
    for i in range(num):
        key = input("Enter the student ID: ")
        value = input("Enter the student name: ")
        dictt[key] = value
    for key, value in dictt.items():
        #check if the value is found in the inverted dictionary
        if value in inverted_dict:
            #if it is found we replace the value with the key and append the keys as values
            inverted_dict[value].append(key)
        else:
            # if it is not found we just change the key into value and the value into a key
            inverted_dict[value] = [key]

    return inverted_dict  
def convertMatrixToDictionary(matrix):
  print("Your matrix is:", matrix)
  dic = {}
  for i in range(len(matrix)):
    key = matrix[i][2]#because we know that the id which will be the key is found at index two
    value = [matrix[i][0], matrix[i][1], matrix[i][3], matrix[i][4]]#the value will be all the other elements found in the rest index's
    dic[key] = value #we create the dictionary

  return "Your dictionary is",dic   