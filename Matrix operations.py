def create(rnc:int):
    """this creates the matrix and is the main function to start up the things"""
    matrix = {}
    for n in range(rnc):
        rowin = input("Enter the row elements(seperated by spaces): ")
        matrix[n+1] = (rowin.split())
        
    prettyprint(matrix)
    return matrix

def add(matrix1:dict , matrix2:dict, rnc:int) -> dict:
    addedmatrix ={}
    for row in matrix1:
        rowlst = []
        for n in range(rnc):
            rowlst.append((int(matrix1[row][n]) + int(matrix2[row][n])))
        addedmatrix[row] = rowlst
    return addedmatrix

def sub(matrix1:dict , matrix2:dict, rnc:int) -> dict:
    subbedmatrix ={}
    for row in matrix1:
        rowlst = []
        for n in range(rnc):
            rowlst.append((int(matrix1[row][n]) - int(matrix2[row][n])))
        subbedmatrix[row] = rowlst
    return subbedmatrix

def multiplication(matrix1, matrix2, rnc):
    rows1 =  matrix1
    column2 = {}
    n=1
    for m in range(rnc):
        column2[(m+1)] = []

    for m in range(rnc): #one loop converts one row into one column of matrix2
        for n in range(rnc):
            column2[m+1].append(matrix2[n+1][m])
    # now we rows of matrix1 and columns of matrix2 
    # now just multiply each element of row with each element of column and add them up
    multimatrix = {}
    for m in range(rnc):
        multimatrix[(m+1)] = []

    element = 0   
    for row in range(rnc):
        for col in range(rnc):
            for eleadd in range(rnc):
                element += int(rows1[row+1][eleadd]) * int(column2[col+1][eleadd])    
            multimatrix[row+1].append(element)
            element = 0
    return multimatrix

def prettyprint(matrix:dict):
    print()
    for row in matrix:
        print(matrix[row])
    print()






print("\nWelcome to Matrix operation Programm\nThis programm can calculate operations on any order square matrix\nHave a good time with it\n")

rnc = int(input("\nEnter order of the square matrix: "))
print("\nCreate First matrix\n")
matrix1 = create(rnc)
print("Create Second matrix\n")
matrix2 = create(rnc)
multiplication(matrix1 , matrix2, rnc)



while True:
    print("ADD[1] SUB[2] MULTIPLICATION[3] Exit[0]\n")
    operation = input("Choose the operation(1:2:3:0): ")
    if operation.strip() == '1':
        addedmatrix = add(matrix1, matrix2, rnc)
        print()
        print("Added Matrix:")
        prettyprint(addedmatrix)
    elif operation.strip() == '2':
        subbedmatrix = sub(matrix1, matrix2, rnc)
        print()
        print("Subbed Matrix:")
        prettyprint(subbedmatrix)
    elif operation.strip() == '3':
        multimatrix = multiplication(matrix1, matrix2, rnc)
        print()
        print("Multiplication of matrix:")
        prettyprint(multimatrix)
    elif operation.strip() == '0':
        break
    else:
        print()
        print("Please enter a valid input")
print()
print("Have a nice day ;)")
    



