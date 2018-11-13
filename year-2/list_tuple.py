#!/usr/bin/python
#
# list_tuple.py bryan
import pprint
pp = pprint.pprint
def One(rng):
	lst = ["#" for x in range(rng)]
	return lst

def Two(a, b):
	lst = [["#" for x in range(a)] for y in range(b)]
	return lst

def Three(a, b, c):
	lst = [[["#" for x in range(a)] for y in range(b)] for z in range(c)]
	return lst

def ThreeMerge(a, b, c):
	lst1 = [[[1 for x in range(a)] for y in range(b)] for z in range(c)]
	lst2 = [[[2 for x in range(a)] for y in range(b)] for z in range(c)]
	return lst1 + lst2

def NatoTuple():
	nato = {"A":"Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta", "E":"Echo", "F":"Foxtrot", "G":"Golf", "H":"Hotel", "I":"India", "J":"Juliet", "K":"Kilo", "L":"Lima", "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa", "Q":"Quebec", "R":"Romeo", "S":"Sierra", "T":"Tango", "U":"Uniform", "V":"Victor", "W":"Whiskey", "X":"Xray", "Y":"Yankee", "Z":"Zulu"}
	return nato

print("1D List:")
pp(One(1))

print("\n2D List:")
pp(Two(2, 2))

print("\n3D List:")
pp(Three(3, 3, 3))

print("\n2x 3D Lists Merged:")
pp(ThreeMerge(3, 3, 3))

print("\nNATO Alphabet Tuple")
pp(NatoTuple())
