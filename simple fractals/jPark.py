from graphics import *
from time import sleep
from random import random

win = GraphWin("JPark", 800, 800)
win2 = GraphWin("DO NOT CLOSE", 1, 1)

counter = 0
maxCount = 50
lineLen = 1

startX = 400
#startX = (2 * lineLen) + 5
startY = 400
#startY = 5

stateList = [0] #0 = R, 1 = L
last_dir = 2 #0 = U, 1 = R, 2 = D, 3 = L

p_1 = Point(startX, startY)
p_2 = Point(startX, startY + 10)

n_line = Line(p_1, p_2)

def draw_line(op, ct, sl, o_dir):
	global maxCount
	global lineLen
	
	p_2 = op
	
	idkwhattocallthis = False
	
	print(ct)
	
	if ct == maxCount:
		return
	else:
		ct += 1
	#
	
	cur_color = color_rgb(random()*255, random()*255, random()*255)
	
	# Drawing StateList
	for i, value in enumerate(sl):
		p_1 = p_2
		if value == 0:
			if o_dir == 0:
				p_2 = Point(p_1.getX() + lineLen, p_1.getY())
				o_dir = 1
				
			elif o_dir == 1:
				p_2 = Point(p_1.getX(), p_1.getY() + lineLen)
				o_dir = 2
				
			elif o_dir == 2:
				p_2 = Point(p_1.getX() - lineLen, p_1.getY())
				o_dir = 3
				
			elif o_dir == 3:
				p_2 = Point(p_1.getX(), p_1.getY() - lineLen)
				o_dir = 0
				
		elif value == 1:
			if o_dir == 0:
				p_2 = Point(p_1.getX() - lineLen, p_1.getY())
				o_dir = 3
				
			elif o_dir == 1:
				p_2 = Point(p_1.getX(), p_1.getY() - lineLen)
				o_dir = 0
				
			elif o_dir == 2:
				p_2 = Point(p_1.getX() + lineLen, p_1.getY())
				o_dir = 1
				
			elif o_dir == 3:
				p_2 = Point(p_1.getX(), p_1.getY() + lineLen)
				o_dir = 2
				
			#
		#
		n_line = Line(p_2, p_1)
		n_line.setFill(cur_color)
		n_line.draw(win)
	#
	
	n_sl = sl[:]
	n_sl.append(0)
	
	for j, value in reversed(list(enumerate(sl))):
		if value == 0:
			n_sl.append(1)
		elif value == 1:
			n_sl.append(0)
		#
	#
	
	print(n_sl)
	
	draw_line(p_2, ct, n_sl, o_dir)
#

n_line.draw(win)

draw_line(p_2, counter, stateList, last_dir)

win2.getMouse()
win.close()