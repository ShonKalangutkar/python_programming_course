import numpy as np

def matrixinput():
    rows = int(input(" Enter number of rows: "))
    cols = int(input(" Enter number of columns: "))
    matrix=[]
    print("Enter the elements row wise: ")
    for i in range(rows):
        row=[]
        for j in range(cols):
            element = float(input(f" Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)

def matrixOperation():
    print("MATRIX CALCULATOR")
    print("1. addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. division")
    
    choice= int(input("Enter the operation number"))
    matrix1 = matrixinput()
    matrix2 = matrixinput()
    
    if choice == 1:
        result=np.add(matrix1, matrix2)
    elif choice == 2:
        result=np.subtract(matrix1, matrix2)
    elif choice == 3:
        result=np.matmul(matrix1, matrix2)
    elif choice == 4:
        result=np.divide(matrix1, matrix2)
    else:
        print("Invalid choice")
        
    print("result")
    print(result)

matrixOperation()