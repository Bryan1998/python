import random
def randlist():
	sentence = "The quick brown fox jumps over the lazy dog".replace(" ", "")
	alphabet = sorted(set(sentence.lower() + sentence.upper()))
	random.shuffle(alphabet)
	print(''.join(alphabet))
for i in range(128):
	randlist()
