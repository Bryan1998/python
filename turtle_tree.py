import turtle
import random

def tree(branchLen,t):
	r = random.randint(5,15)
	if branchLen > 5:
		t.forward(branchLen)
		t.right(30)
		tree(branchLen-r,t)
		t.left(60)
		tree(branchLen-r,t)
		t.right(30)
		t.backward(branchLen)
def main():
	t = turtle.Turtle()
	window = turtle.Screen()
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	t.color("green")
	tree(75,t)
	window.exitonclick()
main()
