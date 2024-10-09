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

mat = transpose(loadtxt(filePath))
X = mat[0]
Y = mat[1]

n = int(sys.argv[2])

Xp  = powers(X,0,n)
Yp  = powers(Y,1,1)
Xpt = Xp.transpose()

a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]

Y2 = []

X2 = []

stepSize = 0.2

minVal = min(X)
maxVal = max(X)
stepAmount = int((maxVal - minVal) / stepSize)

X2 = linspace(minVal,maxVal,stepAmount).tolist()

for xValue in X2:
    temperature = xValue
    predicted_number_of_chirps = poly(a,xValue)
    Y2.append(predicted_number_of_chirps)
    
for i in range(len(X)):
    index = int(i)
print(Y2)

plt.plot(X,Y,'ro')
plt.plot(X2,Y2)
plt.show()