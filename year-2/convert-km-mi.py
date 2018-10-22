# convert-km-mi.py bph

def print_menu():
	print('1: Kilometers to Miles')
	print('2: Miles to Kilometers')

def converter(selector):
	if selector == 1:
		distance = float(input('Enter a distance in Kilometers: '))
		math = distance / 1.60934
	elif selector == 2:
		distance = float(input('Enter a distance in Miles: '))
		math = distance * 1.60934

	print('Converted distance for selection {0}: {1}'.format(selector, math))

if __name__ == '__main__':
	print_menu()
	choice = int(input('Choose a conversion: '))
	converter(choice)
