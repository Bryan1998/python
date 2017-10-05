A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
x = float(input("x: "))
max_x = float(input("max x: "))
while True:
	y = A*x**2 + B*x + C
	print(x,y)
	x = x + 1
	if(x >= max_x+1):
		break
