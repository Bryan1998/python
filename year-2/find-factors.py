# find_factors.py bph

def factors(b):

	for i in range(1, b+1):
		if b % i == 0:
			print(i)

if __name__ == '__main__':

	b = input('Enter a number: ')
	b = float(b)

	if b > 0 and b.is_integer():
		factors(int(b))
	else:
		print('Integer is not positive...')
