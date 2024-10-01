def transpose(matrix):
    transposedMatrix = []
    if matrix == []: return []
    rows = len(matrix)
    columns = len(matrix[0])
    for c in range(columns):
        newRow = []
        for r in range(rows):
            newRow.append(matrix[r][c])
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
    matrix = []
    if not matrixA or not matrixB or not matrixA[0] or not matrixB[0]: return []
    if len(matrixA[0]) != len(matrixB): return []
    for i in range(len(matrixA)):
        newRow = []
        for j in range(len(matrixB[0])):
            sum = 0
            for k in range(len(matrixB)):
                sum  += matrixA[i][k] * matrixB[k][j]
            newRow.append(sum)
        matrix.append(newRow)    
    return matrix

def invert(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    det = a * d - c * b
    invertedMatrix = [[1/det * d, 1/det * -b],[1/det * -c, 1/det * a]]
    return invertedMatrix

def loadtxt(file):
    matrix = []
    with open(file, "r", encoding="utf-8")as f: data = f.readlines()
    cleanData = [i.replace("\n", "") for i in data]
    cleanSplittedData = [i.split("\t") for i in cleanData]
    for row in cleanSplittedData:
        newRow = []
        for element in row: 
            newRow.append(float(element))
        matrix.append(newRow)
    return matrix
