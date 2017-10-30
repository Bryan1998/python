from random import shuffle
def randlist():
	sentence = "The quick brown fox jumps over the lazy dog".replace(" ", "")
	misc = "01234567890 `[]\\;\',./~!@#$%^&*()_+{}|:\"<>?"
	alphabet = sorted(set(sentence.lower() + sentence.upper() + misc))
	shuffle(alphabet)
	print(''.join(alphabet))
randlist()
