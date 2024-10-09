from numpy import *
import sys
import matplotlib.pyplot as plt

def powers(lst, start, end):
    matrix = []
    for element in lst:
        row = []
        for i in range(start, end+1):
            row.append(element**i)
        matrix.append(row)
    return array(matrix) 

def poly(a,x) -> float:
    sum = 0
    for degree,k in enumerate(a):
        sum += k * x**degree

    return float(sum)
    

filePath = sys.argv[1]

dataset = transpose(loadtxt(filePath))
datasetXValues = dataset[0]
datasetYValues = dataset[1]

degree = int(sys.argv[2])



# Beräknar Grafen
Xp  = powers(datasetXValues,0,degree)
Yp  = powers(datasetYValues,1,1)
Xpt = Xp.transpose()

a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]



computedXValues = []
computedYValues = []

stepSize = 0.2

minVal = datasetXValues[0]
maxVal = datasetXValues[-1]
stepAmount = int(ceil((maxVal - minVal) / stepSize))

computedXValues = linspace(minVal,maxVal,stepAmount).tolist()

for xValue in computedXValues:
    currentYValue = poly(a,xValue)
    computedYValues.append(currentYValue)
    
plt.plot(datasetXValues,datasetYValues,'ro')
plt.plot(computedXValues,computedYValues)
plt.show()