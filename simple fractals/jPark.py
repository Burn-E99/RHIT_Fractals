from graphics import *

win = GraphWin("JPark", 800, 800)
win2 = GraphWin("DO NOT CLOSE", 1, 1)

counter = 0
maxCount = 100
lineLen = 10

startX = (2 * lineLen) + 5
startY = 5

n_state = 1

p_1 = Point(startX, startY)

def draw_line(op, ct, ns):
	global maxCount
	global lineLen
	
	print(ct)
	
	if ct == runTimes:
		return
	else:
		ct += 1
	#
	if ns == 1:
		
	elif ns == 2:
		
	elif ns == 3:
		
	elif ns == 4:
		
	elif ns == 5:
		
	elif ns == 6:
		
	elif ns == 7:
		
	elif ns == 8:
		
	elif ns == 9:
		
	elif ns == 10:
		
	elif ns == 11:
			
	elif ns == 12:
		
	elif ns == 13:
		
	elif ns == 14:
		
	elif ns == 15:
		
	elif ns == 16:
		
#

draw_line(p_1, counter, n_state)

win2.getMouse()
win.close()