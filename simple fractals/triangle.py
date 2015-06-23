from graphics import *
from math import *
import time
from random import * 

win = GraphWin("window", 800, 800)

def midpoint(p1, p2):
    return ((p1[0] + p2[0]) /2, (p1[1] + p2[1]) /2)

def matrixmult(m1, m2):
    return [((m1[0] * m2[0]) + (m1[1] * m2[2])), ((m1[0] * m2[1]) + (m1[1] * m2[3])), ((m1[2] * m2[0]) + (m1[3] * m2[2])), ((m1[2] * m2[1]) + (m1[3] * m2[3]))]

def matrixmult2(m1, m2):
    return [((m1[0] * m2[0]) + (m1[1] * m2[1])), ((m1[2] * m2[0]) + (m1[3] * m2[1]))]
    
def midpoint(p1,p2):
    return [((p1[0] + p2[0]) / 2),((p1[1] + p2[1]) / 2)]

redcorner = [600, 600]
bluecorner = [0, 600]
greencorner = [300, 600 -(sqrt(3)/2 * 600)]
corners = [redcorner, bluecorner, greencorner]



randompt = [400, 400]#[randint(200,600), randint(200,600)]
ox = randompt[0]
oy = randompt[1]
    
a = .5
b = .5
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



for i in range(100000):
    
    
    
    randcorner = corners[randint(0, 2)]
    bi = [randcorner[0]/2, randcorner[1]/2]
    
    Ti = matrixmult2(a1, xy)
    Ti1 = [Ti[0] + bi[0], Ti[1] + bi[1]]
    
    point1 = Point(Ti1[0], Ti1[1])
    point1.draw(win)
    xy = [Ti1[0], Ti1[1]]
    i += 1
    print(Ti1, randcorner)

        
    





    

