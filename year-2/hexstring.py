# hexstring.py bryan

def bincon(decimal):
	print(decimal)
	print("BIN ********")
	binstr = "" # binstr is a string
	for i in range(8):
		bin = decimal % 2
		decimal = decimal // 2
		binstr = binstr + str(bin)
	print("----")
	print(binstr[::-1])
	
def hexcon(decimal):
	print(decimal)
	print("HEX ********")
	# dividend / divisor = quotient
	hexstr = "" # hexstr is a string
	# ------------------------------------------
	remainder = decimal % 16
	if remainder == 10:
		remainder = "A"
	elif remainder == 11:
		remainder = "B"
	elif remainder == 12:
		remainder = "C"
	elif remainder == 13:
		remainder = "D"
	elif remainder == 14:
		remainder = "E"
	elif remainder == 15:
		remainder = "F"
	# ------------------------------------------
	quotient = decimal // 16
	if quotient == 10:
		quotient = "A"
	elif quotient == 11:
		quotient = "B"
	elif quotient == 12:
		quotient = "C"
	elif quotient == 13:
		quotient = "D"
	elif quotient == 14:
		quotient = "E"
	elif quotient == 15:
		quotient = "F"
	# ------------------------------------------
	hexstr = str(quotient) + " " + str(remainder)
	print("----")
	print(hexstr)
	
def main():
	print("TYPE -1 TO EXIT THE PROGRAM")
	print("TYPE A POSIIVE INTEGER LESS THAN 256")
	done = 0
	
	while (done >= 0):
		dec = input("INTEGER: ")
		bincon(dec)
		hexcon(dec)
		print("DONE")

main()
