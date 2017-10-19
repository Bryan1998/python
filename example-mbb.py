from graphics import *
def main():
	win = GraphWin('Body', 512, 512) 
	win.yUp() 
	win.setBackground('red') #Bryan H

	head = Circle(Point(69,120), 27) 
	head.setWidth(9)
	head.setFill("green")
	head.draw(win)

	head = Circle(Point(25,370), 35)
	head.setWidth(7) 
	head.setFill("yellow")
	head.draw(win)

	eye1 = Circle(Point(100, 98), 8)
	eye1.setWidth(6)
	eye1.setFill('pink')
	eye1.draw(win)

	head = Circle(Point(56, 135), 6) 
	head.setWidth(5)
	head.setFill("Light Blue")
	head.draw(win)

	mouth = Circle(Point(45, 118), 5) 
	mouth.setWidth(6)
	mouth.draw(win)
	body = Line(Point(70, 100), Point(0, -256))
	body.setWidth(5)
	body.setFill("pink")
	body.draw(win)

	body = Line(Point(55, 55), Point(67, 89))
	body.setWidth(7)
	body.setFill("Pink")
	body.draw(win)

	body = Line(Point(45, 45), Point(67, 89))
	body.setWidth(7)
	body.setFill("Lime Green")
	body.draw(win)

	hell = Line(Point(200, 200), Point(220,360))
	hell.setWidth(7)
	hell.setFill("Gray")
	hell.draw(win)
	
	label = Text(Point(320, 128), 'THIS IS THE HIGHWAY TO... where?')
	label.draw(win)
	
	label2 = Text(Point(100, 39), 'Mine is really bad')
	label2.draw(win)
	
	win.getMouse()
	win.close()
main()
