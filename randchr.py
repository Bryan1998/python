# some random character stuff
from random import randint
def rint():
	r = randint(64,122)
	if (r==64):
		r = 42
	return r
	
def main():
	for i in range (65535):
		z = rint()
		print(chr(z),end="")
main()
