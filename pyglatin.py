def main():
	words = input('Enter some words: ').split()
	for word in words:
		if word[0] in ['a','e','i','o','u']:
			print(word[1:] + word[0] + "yay", end = " ")
		else:
			print(word[1:] + word[0] + "ay", end = " ")
	print()
main()
