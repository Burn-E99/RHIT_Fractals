from graphics import *
from math import *
from time import sleep

win = GraphWin("Cool Tree", 1600, 800, autoflush=False)
win2 = GraphWin("DO NOT CLOSE", 1, 1)

runTimes = 20
count = 0
ratio = 7/8
angle = pi/6
breakangle = pi/2
breakratio = 1/3
widthratio = (runTimes - 3)/runTimes
breakwidrat = (runTimes / 2)/runTimes
width = runTimes
totCt = 0

def draw_line(sp, ep, ol, na, ct, wi):
	global angle
	global breakangle
	global ratio
	global runTimes
	global widthratio
	global totCt
	
	totCt +=1
	
	print(ct)
	print(totCt)
	
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
	new_line.setWidth(wi)
	new_line.draw(win)
	
	if totCt%10000 == 0:
		win.update()
		print("updated")
	
	
	draw_line(n_p1, n_p2, nl * ratio, na - angle, ct, wi * widthratio)
	draw_line(n_p1, n_p2, nl * breakratio, na + breakangle, ct, wi * breakwidrat)
#

sp_1 = Point(0, 0)
sp_2 = Point(800, 800)

draw_line(sp_1, sp_2, 200, -pi/2, count, width)

win.update()
win2.getMouse()
win.close()