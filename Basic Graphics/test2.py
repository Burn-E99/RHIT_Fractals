from graphics import *
from math import *
from random import *

width = 1000
height = 800

startX = width / 2
startY = height
startL = 300
runTimes = 18

win = GraphWin("Tree", width, height)
win2 = GraphWin("DO NOT CLOSE", 1, 1)

counter = 0
ratio = 2/3
angle = -pi/4

def m_draw(sp, ep, ol, na, counter): # sp=OLD Start pt, ep=OLD End pt, ol=OLD Length, oa=OLD Angle
	global angle
	global ratio
	global runTimes
	
	print(counter)
	
	if counter == runTimes:
		return
	else:
		counter += 1
	#
	
	nl = ol * ratio
	
	dX = nl * cos(na)
	dY = nl * sin(na)
	
	n_p1 = ep
	n_p2 = Point(dX + ep.getX(), dY + ep.getY())
	
	new_line = Line(n_p1, n_p2)
	new_line.setFill("green")
	m_line.setWidth(2)
	new_line.draw(win)
	
	#code
	m_draw(n_p1, n_p2, nl, na - angle, counter)#right
	m_draw(n_p1, n_p2, nl, na + angle, counter)#left
#

o_p1 = Point(startX, startY)
o_p2 = Point(startX, height - startL)

m_line = Line(o_p1, o_p2)
m_line.setFill("brown")
m_line.setWidth(8)
m_line.draw(win)

m_draw(o_p1, o_p2, startL, angle, counter)
m_draw(o_p1, o_p2, startL, 3 * angle, counter)

win2.getMouse()
win.close()