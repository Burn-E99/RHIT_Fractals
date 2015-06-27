from graphics import *
from random import *

win = GraphWin("Seirpinski Triangle", 810, 810)
win2 = GraphWin("DO NOT CLOSE", 1, 1)

s_a = Point(405,5)
s_b = Point(5,805)
s_c = Point(805,805)

runTimes = 10
ct = 0
colored = True

def draw_triangle(m_a, m_b, m_c, ct):
	global runTimes
	global colored
	
	print(ct)
	
	if ct == runTimes:
		return
	else:
		ct += 1
	#
	
	line_b = Line(m_a, m_b)
	line_c = Line(m_a, m_c)
	line_d = Line(m_b, m_c)
	
	if colored:
		line_b.setFill(color_rgb(random()*255, random()*255, random()*255))
		line_c.setFill(color_rgb(random()*255, random()*255, random()*255))
		line_d.setFill(color_rgb(random()*255, random()*255, random()*255))
	#
	
	line_b.draw(win)
	line_c.draw(win)
	line_d.draw(win)
	
	l_b_mp = line_b.getCenter()
	l_c_mp = line_c.getCenter()
	l_d_mp = line_d.getCenter()
	
	draw_triangle(m_a, l_b_mp, l_c_mp, ct) # Triangle 1
	draw_triangle(l_b_mp, m_b, l_d_mp, ct) # Triangle 2
	draw_triangle(l_c_mp, l_d_mp, m_c, ct) # Triangle 3
#

draw_triangle(s_a, s_b, s_c, ct)

win2.getMouse()
win.close()