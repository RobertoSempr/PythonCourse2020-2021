

# libreria
import math
# input cateti
c1 = float(input("Cat 1?"))
c2 = float(input("Cat 2?"))
# calcoli
i = math.sqrt(c1**2+c2**2)
A = c1*c2/2
P = c1+c2+i
# output
print("ipotenusa = ", i)
print("area = ", A)
print("perimetro = ", P)
