#dechexbin_loop.py bryan

def bincon(decimal):
	bin_str = ""
	for i in range(8):
		binary = str(decimal % 2)
		decimal = decimal // 2
		bin_str = bin_str + str(binary)
		if i == 3:
			bin_str = bin_str + " "
	return bin_str[::-1]

def hexcon(decimal):
	hex_str = ""
	if decimal % 16 > 9:
		add_asc = 55
	else:
		add_asc = 48
	remainder = str(chr((decimal % 16) + add_asc))
	
	if decimal // 16 > 9:
		add_asc = 55
	else:
		add_asc = 48
	quotient = str(chr((decimal // 16) + add_asc))
	
	hex_str = quotient + remainder
	return hex_str

def main():
	dec = 0
	while dec < 256:
		hex_s = hexcon(dec)
		bin_s = bincon(dec)
		print(dec,hex_s,bin_s)
		dec += 1
	
main()
