

def transpose(matrix):
    transposedMatrix = []
    if matrix == []: return []
    rows = len(matrix)
    columns = len(matrix[0])
    for c in range(columns):
        newRow = []
        for r in range(rows):
            newRow.append(matrix[r][c])
            print(newRow)
        transposedMatrix.append(newRow)
    return transposedMatrix



def powers(lst, start, end):
    matrix = []
    for element in lst:
        row = []
        for i in range(start, end+1):
            row.append(element**i)
        matrix.append(row)
    return matrix 


def matmul(matrixA, matrixB):
    newMatrix = []
    newRow = []

    if not matrixA or not matrixB or not matrixA[0] or not matrixB[0]: return []
    columnLenA, rowLenA, rowLenB, columnLenB = len(matrixA[0]), len(matrixA), len(matrixB), len(matrixB[0])

    if columnLenA != rowLenB: return []

    for r in range(rowLenA):
        
        for c in range(columnLenA):
            element = 0
            for i in range(columnLenB):
                element += matrixA[r][i] * matrixB[i][r]
            newRow.append(element)
    newMatrix.append(newRow)
    newRow = []

    return newMatrix

print(matmul([[1,2],[3,4],[5,6]],[[1,1,1],[1,1,1]]))



def invert():
    pass
def loadtxt(file):
    pass