from graphics import *
from math import *
from random import *
import time

win = GraphWin("This is a thingy", 500, 500)

cX, cY = 250, 250
side = 200
inRad = side/2
outRad = side/sqrt(2)
dt = .05

center = Point(cX, cY)
corner1 = Point(cX, cY - outRad)
corner2 = Point(cX + outRad, cY)
corner3 = Point(cX, cY + outRad)
corner4 = Point(cX - outRad, cY)

thing = Polygon(corner1, corner2, corner3, corner4)
inner = Circle(center, inRad)
outer = Circle(center, outRad)

outer.draw(win)
thing.draw(win)
inner.draw(win)

win.getMouse()
win.close()