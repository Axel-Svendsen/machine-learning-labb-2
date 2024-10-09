from matrix import *
import matplotlib.pyplot as plt
import sys

filePath = sys.argv[1]

mat = transpose(loadtxt(filePath))
X = mat[0]
Y = mat[1]


Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

Y2 = []
for xValue in X:
    temperature = xValue
    predicted_number_of_chirps = b + m * temperature
    Y2.append(predicted_number_of_chirps)

plt.plot(X,Y,'ro')
plt.plot(X,Y2)
plt.show()