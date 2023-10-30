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