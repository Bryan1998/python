#!/usr/bin/python3
from random import shuffle
import string
from sys import argv
def main():
	letters = list(string.ascii_letters)
	symbols = list(string.punctuation)
	numbers = list(string.digits)
	char = sorted(set(numbers + symbols + letters))
	shuffle(char)
	return "".join(char)
while True:
	if argv == True:
		pos_int = argv[1]
	elif argv == IndexError:
		pos_int = input("positive integer: ")
	try:
		val = int(pos_int)
		if val < 0:
			print("error: negative integer")
			continue
		break
	except ValueError:
		print("error: not an integer")
	break
print("\n")
for i in range(val):
	print(main())
print("\ndone")
