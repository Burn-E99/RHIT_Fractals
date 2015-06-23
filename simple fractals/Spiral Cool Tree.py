from graphics import *
from math import *
from time import sleep

win = GraphWin("Cool Tree", 800, 800)
win2 = GraphWin("DO NOT CLOSE", 1, 1)

runTimes = 15
count = 0
ratio = 3/4
angle = pi/3
breakangle = pi/2
breakratio = 1/3

def draw_line(sp, ep, ol, na, ct):
	global angle
	global breakangle
	global ratio
	global runTimes
	
	print(ct)
	
	if ct == runTimes:
		return
	else:
		ct += 1
	#
	
	nl = ol
	
	dX = nl * cos(na)
	dY = nl * sin(na)
	
	n_p1 = ep
	n_p2 = Point(dX + ep.getX(), dY + ep.getY())
	
	new_line = Line(n_p1, n_p2)
	new_line.draw(win)
	
	draw_line(n_p1, n_p2, nl * ratio, na - angle, ct)
	draw_line(n_p1, n_p2, nl * breakratio, na + breakangle, ct)
#

sp_1 = Point(0, 0)
sp_2 = Point(400, 800)

draw_line(sp_1, sp_2, 300, -pi/2, count)

win2.getMouse()
win.close()