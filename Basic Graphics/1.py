from graphics import *
from math import *
from random import *
import time

def change_color():
	inner.setFill(color_rgb(random()*255, random()*255, random()*255))
	time.sleep(dt)
	square.setFill(color_rgb(random()*255, random()*255, random()*255))
	time.sleep(dt)
	outer.setFill(color_rgb(random()*255, random()*255, random()*255))
	time.sleep(dt)
	change_color()

win = GraphWin("This is a thingy", 500, 500)
win2 = GraphWin("This is a thingy 2", 1, 1)

cX, cY = 250, 250
side = 200
inRad = side/2
outRad = side/sqrt(2)
dt = .05

center = Point(cX, cY)
corner1 = Point(cX + (side/2), cY + (side/2))
corner2 = Point(cX - (side/2), cY - (side/2))

square = Rectangle(corner1, corner2)
inner = Circle(center, inRad)
outer = Circle(center, outRad)

outer.draw(win)
square.draw(win)
inner.draw(win)

change_color()

win2.getMouse()
win.close()