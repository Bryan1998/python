#binarystring.py bryan

def bincon(decimal):
	#print(decimal)
	print("************")
	binstr = ""
	decimal = int(decimal)
	
	if decimal >= 256:
		print("INTEGER IS OVER 256")
		
	elif decimal == -1:
		print("EXIT REQUESTED")
		exit()
		
	elif decimal != int(decimal):
		print("NOT AN INTEGER")
		
	else:
		for i in range(len(bin(decimal)) - 1):
			bin_bin = decimal % 2
			decimal = decimal // 2
			binstr = binstr + str(bin_bin)
			#print(i)
			print(binstr[::-1])


def main():
	print("TYPE -1 TO EXIT THE PROGRAM")
	print("TYPE A POSIIVE INTEGER LESS THAN 256")
	done = 0
	
	while (done >= 0):
		dec = input("INTEGER: ")
		bincon(dec)
		print("DONE")


main()
