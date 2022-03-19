def performOperationOnMatrix(matrix1, matrix2):
    
    # checking is addition and subtraction is possible or not
    def isAdditionAndSubtractionPossible(matrix1, matrix2):
        return matrix1.__len__() != 0 and matrix2.__len__() != 0 and matrix1.__len__() == matrix2.__len__() and matrix1[0].__len__() == matrix2[0].__len__()
    
    # performing addition
    def performAndPrintAddition(matrix1, matrix2):
        if isAdditionAndSubtractionPossible(matrix1, matrix2):
            for i in range(matrix1.__len__()):
                for j in range(matrix1[0].__len__()):
                    print(matrix1[i][j] + matrix2[i][j], end="\t")
                print()
        else:
            print("Addition is not possible") 
    
    # performing subtraction
    def performAndPrintSubtraction(matrix1, matrix2):
        if isAdditionAndSubtractionPossible(matrix1, matrix2):
            for i in range(matrix1.__len__()):
                for j in range(matrix1[0].__len__()):
                    print(matrix1[i][j] - matrix2[i][j], end="\t")
                print()
        else:
            print("Subtraction is not possible") 

    # performing multiplication
    def performAndPrintMultiplication(matrix1, matrix2):
        if matrix1.__len__() != 0 and matrix2.__len__() != 0 and matrix1[0].__len__() == matrix2.__len__():
            k = 0
            for i in range(matrix1.__len__()):
                ans = 0
                for j in range(matrix2[0].__len__()):
                    for k in range(matrix2.__len__()):
                        ans += matrix1[i][k] * matrix2[k][j]
                    print(ans, end="\t")
                    k += 1
                    ans = 0
                k = 0
                print()
        else:
            print("Multiplication is not possible") 
    
    # check if is symmetric
    def checkIfSymmetric(matrix):
        return matrix.__len__() == matrix[0].__len__()
    
    # check if binary
    def checkIfBinary(matrix):
        for row in matrix:
            for number in row:
                if number != 0 or number != 1:
                    return False
        return True
    
    print()
    performAndPrintAddition(matrix1, matrix2)
    print()
    performAndPrintSubtraction(matrix1, matrix2)
    print()
    performAndPrintMultiplication(matrix1, matrix2)
    print()

    return [checkIfSymmetric(matrix1), checkIfSymmetric(matrix2), checkIfBinary(matrix1), checkIfBinary(matrix2)]


# getting data for first matrix
def getDataForFirstMatrix():
    rows = int(input("Enter number of rows for first matrix:\t"))
    columns = int(input("Enter number of columns for first matrix:\t"))
    matrix = []
    print("Enter values for first matrix: ")
    for _ in range(rows):
        l = []
        for _ in range(columns):
            l.append(int(input()))
        matrix.append(l)
    return [rows, columns, matrix]


# getting data for second matrix
def getDataForSecondMatrix():
    rows = int(input("Enter number of rows for second matrix:\t"))
    columns = int(input("Enter number of columns for second matrix:\t"))
    matrix = []
    print("Enter values for first matrix: ")
    for _ in range(rows):
        l = []
        for _ in range(columns):
            l.append(int(input()))
        matrix.append(l)
    return [rows, columns, matrix]


# Getting two matrices
rows1, columns1, matrix1 = getDataForFirstMatrix()
rows2, columns2, matrix2 = getDataForSecondMatrix()
# performing functions on matrices
symmetricAndBinaryData = performOperationOnMatrix(matrix1, matrix2)
print("Is matrix 1 symmetric:\t", symmetricAndBinaryData[0])
print("Is matrix 2 symmetric:\t", symmetricAndBinaryData[1])
print("Is matrix 1 binary:\t", symmetricAndBinaryData[2])
print("Is matrix 2 binary:\t", symmetricAndBinaryData[3])
print()

'''
3
2
1
2
3
4
5
6
2
3
10
11
20
21
30
31
'''

'''
2
2
1
2
3
4
2
2
4
3
2
1
'''

'''
1 2
3 4

4 3
2 1
'''