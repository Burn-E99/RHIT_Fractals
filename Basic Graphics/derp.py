## simulation of rols of two dice with graphical display
## Allen Broughton 17 Jun 15

# load packages 
from random import *
from graphics import *
from math import *
import time

#set parameters
# probs = [1/6,1/6,1/6,1/6,1/6,1/6] # fair die
# probs = [1/9,2/9,1/9,2/9,1/9,2/9] # prob even =twice prob odd
probs = [1/21,2/21,3/21,4/21,5/21,6/21] # prob proportional to dieface 
numrolls = 10000
skip = 500
print("numrolls = ",numrolls, "skip = ",skip)
print("totalprob = ",sum(probs))


#probability setup
#setup cumulative probabilities and define rolldie
cumprobs = [];
cp = 0
for j in range(len(probs)):
    cp = cp+probs[j]
    cumprobs.append(cp)       # add to the end of the list  
cumprobs[len(cumprobs)-1] = 1 # ensure total probability exactly 1
    
def rolldie():
    p = random()
    j=0
    while p > cumprobs[j]:
        j=j+1
    return j+1

# set up counters
dicerollcount = [[0 for j in range(6)] for k in range(6)]


# graphics setup
dicewin = GraphWin("Diceroll distribution", 500,500)
# set up parameters
x0 = 100
y0 = 100
dx = 50
dy = 50
black = color_rgb(0,0,0)
white = color_rgb(255,255,255)
scale = 255*36/2
dt =0.02
# define graphic objects and functions
cells =[]
for j in range(6):
    row =[]
    for k in range(6):
        square = Rectangle(Point(x0+k*dx,y0+j*dy),Point(x0+(k+1)*dx,y0+(j+1)*dy))
        square.setFill(black)
        square.draw(dicewin)
        row.append(square)
        time.sleep(dt)
    cells.append(row)
     
def gray(x):
    xr = max(0,min(255,int(x)))
    return color_rgb(xr,xr,xr)


def updatecells(throws):
    for j in range(6):
        for k in range(6):
            cells[j][k].setFill(gray(scale*(dicerollcount[j][k])/throws))
            time.sleep(dt)
        
#run diceroll experiment
print("starting experiment")

for n in range(numrolls):
    j = rolldie()-1
    k = rolldie()-1
    dicerollcount[j][k] = dicerollcount[j][k]+1
    if n % skip == 0 and n > 0:
        print("updating, numthrows=",n)
        updatecells(n)
        time.sleep(0.5)