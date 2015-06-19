from graphics import *
from math import *
from random import *
import time


win = GraphWin("window", 800, 800)
counter = 0
Colored = True
border = "white"
win.setBackground(border)
counterMax = 6

def tSquare(ocentx, ocenty, osize, counter, m_dir):
    global counterMax
    global border
    global Colored
    
    if counter == counterMax:
        return
    else:
        counter += 1
    #
    if m_dir == 1:
        ncentx = ocentx - osize /2
        ncenty = ocenty - osize / 2
        size = osize / 2
        newcentx = ocentx - osize / 4 
        newcenty = ocenty - osize / 4
        np_1 = Point(newcentx  , newcenty )
        np_2 = Point(newcentx - size , newcenty - size)
        nsquare = Rectangle(np_2, np_1)
        if Colored: nsquare.setFill(color_rgb(random()*255, random()*255, random()*255))
        nsquare.setOutline(border)
        nsquare.draw(win)
		
        tSquare(ncentx, ncenty, size, counter,1)
        tSquare(ncentx, ncenty, size, counter,2)
        tSquare(ncentx, ncenty, size, counter,4)
        
    elif m_dir == 2:
        ncentx = ocentx + osize /2
        ncenty = ocenty - osize / 2
        size = osize / 2
        newcentx = ocentx + osize / 4 
        newcenty = ocenty - osize / 4
        np_1 = Point(newcentx  , newcenty )
        np_2 = Point(newcentx + size , newcenty - size)
        nsquare = Rectangle(np_2, np_1)
        if Colored: nsquare.setFill(color_rgb(random()*255, random()*255, random()*255))
        nsquare.setOutline(border)
        nsquare.draw(win)
        
        tSquare(ncentx, ncenty, size, counter,1)
        tSquare(ncentx, ncenty, size, counter,2)
        tSquare(ncentx, ncenty, size, counter,3)
        
    elif m_dir == 3:
        ncentx = ocentx + osize /2
        ncenty = ocenty + osize / 2
        size = osize / 2
        newcentx = ocentx + osize / 4 
        newcenty = ocenty + osize / 4
        np_1 = Point(newcentx  , newcenty )
        np_2 = Point(newcentx + size , newcenty + size)
        nsquare = Rectangle(np_2, np_1)
        if Colored: nsquare.setFill(color_rgb(random()*255, random()*255, random()*255))
        nsquare.setOutline(border)
        nsquare.draw(win)
        
        tSquare(ncentx, ncenty, size, counter,4)
        tSquare(ncentx, ncenty, size, counter,2)
        tSquare(ncentx, ncenty, size, counter,3)
    elif m_dir == 4:
        ncentx = ocentx - osize /2
        ncenty = ocenty + osize / 2
        size = osize / 2
        newcentx = ocentx - osize / 4 
        newcenty = ocenty + osize / 4
        np_1 = Point(newcentx  , newcenty )
        np_2 = Point(newcentx - size , newcenty + size)
        nsquare = Rectangle(np_2, np_1)
        if Colored: nsquare.setFill(color_rgb(random()*255, random()*255, random()*255))
        nsquare.setOutline(border)
        nsquare.draw(win)
        
        tSquare(ncentx, ncenty, size, counter,1)
        tSquare(ncentx, ncenty, size, counter,4)
        tSquare(ncentx, ncenty, size, counter,3)
#
        
point1 = Point(500, 500)
point2 = Point(300, 300)
square = Rectangle(point1, point2)
square.draw(win)
tSquare(400, 400, 200, counter,1)
tSquare(400, 400, 200, counter,2)
tSquare(400, 400, 200, counter,3)
tSquare(400, 400, 200, counter,4)
win.getMouse()
win.close()


