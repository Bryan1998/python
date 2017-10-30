from cmath import sqrt

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

calc = (b**2) - (4*a*c)
sol1 = (-b + sqrt(calc)) / (2*a)

print('%0.4f ± %0.4fi' % (sol1.real, sol1.imag))
