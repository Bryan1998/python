# some random character shit
from random import randint
def rint():
	r = randint(65,122)
	if r in range(65,122):
		return r
		
def main():
	for i in range (65535):
		z = rint()
		print(chr(z),end="")
main()
