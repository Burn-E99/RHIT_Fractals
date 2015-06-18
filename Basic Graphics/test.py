from graphics import *
from math import *
from random import *

def drawLines():
	point1 = Point(50, 700/2)
	point2 = Point(650, 700/2)
	m_len = 600
	m_dir = 0
	m_line = Line(point1, point2)
	m_line.setFill(color_rgb(random()*255, random()*255, random()*255))
	m_line.draw(win)
	
	for i in range(0, 120):
		time.sleep(.1)
		c = m_line.getCenter()
		nP1 = Point(c.getX(), c.getY())
		
		m_len /= 2 # m_len = m_len / 2
		
		m_line.setWidth(2)
		
		if m_dir == 0:
			m_dir = 1
			nP2 = Point(c.getX(), c.getY() - m_len)
			m_line = Line(nP1, nP2)
			m_line.setFill(color_rgb(random()*255, random()*255, random()*255))
			m_line.draw(win)
			continue
		elif m_dir == 1:
			m_dir = 2
			nP2 = Point(c.getX() + m_len, c.getY())
			m_line = Line(nP1, nP2)
			m_line.setFill(color_rgb(random()*255, random()*255, random()*255))
			m_line.draw(win)
			continue
		elif m_dir == 2:
			m_dir = 3
			nP2 = Point(c.getX(), c.getY() + m_len)
			m_line = Line(nP1, nP2)
			m_line.setFill(color_rgb(random()*255, random()*255, random()*255))
			m_line.draw(win)
			continue
		elif m_dir == 3:
			m_dir = 0
			nP2 = Point(c.getX() - m_len, c.getY())
			m_line = Line(nP1, nP2)
			m_line.setFill(color_rgb(random()*255, random()*255, random()*255))
			m_line.draw(win)
			continue
	#
	time.sleep(.05)
	drawLines()

win = GraphWin("test", 700, 700)

drawLines()

win.getMouse()
win.close()