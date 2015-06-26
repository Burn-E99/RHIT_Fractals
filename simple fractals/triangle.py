from graphics import *
from math import *
import time
from random import * 

changexloc = 450
changeyloc = 450

runtimes = 500000

win = GraphWin("window", 810, 810)

from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw

image = Image.new("RGB", (810, 810), color=(255,255,255,0)) # w,h
draw = ImageDraw.Draw(image)

show = not True

if not show:
	derp = Point(100,100)
	noshow = Text(derp, "NO DRAWING")
	noshow.draw(win)


def midpoint(p1, p2):
    return ((p1[0] + p2[0]) /2, (p1[1] + p2[1]) /2)

def matrixmult(m1, m2):
    return [((m1[0] * m2[0]) + (m1[1] * m2[2])), ((m1[0] * m2[1]) + (m1[1] * m2[3])), ((m1[2] * m2[0]) + (m1[3] * m2[2])), ((m1[2] * m2[1]) + (m1[3] * m2[3]))]

def matrixmult2(m1, m2):
    return [((m1[0] * m2[0]) + (m1[1] * m2[1])), ((m1[2] * m2[0]) + (m1[3] * m2[1]))]
    
def midpoint(p1,p2):
    return [((p1[0] + p2[0]) / 2),((p1[1] + p2[1]) / 2)]

redcorner = [405, 5]
bluecorner = [25, 281]
greencorner = [170, 729]
yellowcorner = [640, 729]
orangecorner = [785, 281]

redcorner = [5, 805]
bluecorner = [805,805]
greencorner = [405, 5]

redcorner = [150, 650]
bluecorner = [650, 650]
greencorner = [405, 155]

corners = [redcorner, bluecorner, greencorner]



randompt = [randint(200,600), randint(200,600)]
ox = randompt[0]
oy = randompt[1]
    
a = -2/3
b = -2/3
t = 0
th = 0
rot = [cos(th), -sin(th), sin(th), cos(th)]
sheer = [1, t, 0, 1]
scal = [a, 0, 0, b]
xy = [ox, oy]
m1 = matrixmult(rot, scal)
a1 = matrixmult(m1, sheer)


bi1 = (1/2, 0)
bi2 = (0, 0)
bi3 = (0 / 1/2)
t1 = [a1, bi1]
t2 = [a1, bi2]
t3 = [a1, bi3]
tlist = [t1, t2, t3]
randt = tlist[randint(0,2)]



for i in range(runtimes):
    randcorner = corners[randint(0, (len(corners)-1))]
    bi = [randcorner[0]/(len(corners)-1), randcorner[1]/(len(corners)-1)]
    
    Ti = matrixmult2(a1, xy)
    Ti1 = [Ti[0] + bi[0] + changexloc, Ti[1] + bi[1] + changeyloc]
    
    point1 = Point(Ti1[0], Ti1[1])
    if show:
	    point1.draw(win)
    draw.point([point1.getX(), point1.getY()], (0,0,0))
    xy = [Ti1[0], Ti1[1]]
    i += 1
    print(Ti1, randcorner)
    print(i)
#

image.save("image1" + str(random()) + ".png", "PNG")

win.getMouse()
win.getMouse()
win.getMouse()
win.getMouse()
win.getMouse()
win.getMouse()
win.getMouse()
win.getMouse()
win.getMouse()