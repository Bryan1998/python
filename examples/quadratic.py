#!/usr/bin/python3

def roots(a,b,c):
	D = (b*b - 4*a*c)**0.5 # DISCRIMINANT
	x_1 = (-b + D) / (2 * a)
	x_2 = (-b - D) / (2 * a)
	print('x1: {0}'.format(x_1))
	print('x2: {0}'.format(x_2))

if __name__ == '__main__':
	a = int(input("Enter A: "))
	b = int(input("Enter B: "))
	c = int(input("Enter C: "))
	roots(float(a),float(b),float(c))
