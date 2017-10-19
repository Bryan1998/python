from graphics import *


def main():
    win = GraphWin('Body', 1000, 1000) 
    win.yUp() 

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
    body = Line(Point(70, 100), Point(0, -10000))
    body.setWidth(5)
    body.setFill("red")
    body.draw(win)
    
    body = Line(Point(55, 55), Point(67, 89))
    body.setWidth(7)
    body.setFill("Pink")
    body.draw(win)
    
    body = Line(Point(45, 45), Point(67, 89))
    body.setWidth(7)
    body.setFill("Lime Green")
    body.draw(win)

    label = Text(Point(100, 39), 'Mine is really bad')
    label.draw(win)
    win.getMouse()
    win.close()
	    


main()
