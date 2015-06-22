from graphics import *
from math import *
from random import random

win = GraphWin("Seirpinski V2", 810, 810)
win2 = GraphWin("DO NOT CLOSE", 1, 1)

ptA = Point(405, 5)
ptB = Point(5, 805)
ptC = Point(805, 805)

ptList = [ptA, ptB, ptC]
colList = ["red", "green", "blue"]

count = 0
maxCt = 900

ptA.draw(win)
ptB.draw(win)
ptC.draw(win)

last_pt = Point(0, 0)

def pick_corner():
	c = trunc(random()*3)
	return c

def draw_pt(op, ct):
	global ptList
	global colList
	global maxCt
	global last_pt
	
	print(ct)
	
	if ct == maxCt:
		return
	else:
		ct += 1
	#
	
	curCorner = pick_corner()
	tempLine = Line(ptList[curCorner], op)
	new_pt = tempLine.getCenter()
	new_pt.setFill(colList[curCorner])
	new_pt.draw(win)
	
	last_pt = new_pt
	
	draw_pt(new_pt, ct)
#

startPt = Point(400, 400)

draw_pt(startPt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)
draw_pt(last_pt, count)

win2.getMouse()
win.close()